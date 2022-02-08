from flask import Flask, render_template, url_for, request, abort, redirect
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from form import SignUpForm, LoginForm


app = Flask(__name__)
app.config.from_object(DevConfig)


# ROUTES
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Homepage")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    return render_template("signup.html", title="Sign Up", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5000, load_dotenv=True)
