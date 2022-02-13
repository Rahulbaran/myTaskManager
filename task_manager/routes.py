from flask import render_template, redirect, url_for
from . import app, db, bcrypt
from .form import SignUpForm, LoginForm
from .models import User


# ROUTES
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Homepage")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(fullname=form.fullname.data, username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("signup.html", title="Sign Up", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)
