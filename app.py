import os
from flask import Flask, render_template, url_for, request, abort, redirect, render_template_string
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(16).hex()


# ROUTES
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Homepage")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html", title="Sign Up")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", title="Login")


if __name__ == "__main__":
    app.run(debug=True, port=5000, load_dotenv=True)
