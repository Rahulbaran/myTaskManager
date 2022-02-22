from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from . import app, db, bcrypt
from .form import SignUpForm, LoginForm
from .models import User


# ROUTES
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Homepage")


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
