from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from . import app, db, bcrypt
from .form import SignUpForm, LoginForm
from .models import User, Note


# ROUTES
@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    notes = ""
    if current_user.is_authenticated:
        notes = Note.query.filter_by(userNote=current_user).order_by(Note.id.desc()).all()
        if request.method == "POST":
            noteData = request.get_json()
            newNote = Note(title=noteData.get("title"), content=noteData.get("content"), user_id=current_user.id)
            db.session.add(newNote)
            db.session.commit()
            note = Note.query.filter_by(user_id=current_user.id).order_by(Note.id.desc()).first()
            return {
                "id": note.id,
                "title": note.title,
                "content": note.content,
                "note_date": note.created_on.strftime("%d/%m/%Y"),
            }
    return render_template("home.html", title="Homepage", notes=notes)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(fullname=form.fullname.data, username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("You have registered successfully, now you can login", "info")
        return redirect(url_for("login"))
    return render_template("signup.html", title="Sign Up", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            next = request.args.get("next")
            login_user(user, remember=form.remember_me.data)
            flash(f"Welcome {user.fullname}, You have logged in", "info")
            return redirect(next) if next else redirect(url_for("home"))
        else:
            flash("Either email or password is wrong", "warning")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logout successfully", "info")
    return redirect(url_for("home"))


@app.route("/settings")
@login_required
def settings():
    return render_template("settings.html", title="Settings")
