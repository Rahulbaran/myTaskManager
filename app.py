from flask import Flask, render_template, url_for, request, abort, redirect, render_template_string
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# ROUTES
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000, load_dotenv=True)
