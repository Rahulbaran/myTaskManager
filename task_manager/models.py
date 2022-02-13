from datetime import datetime
from . import db


# MODELS
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fullname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    joined_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    avatar = db.Column(db.String(40), default="avatar.png", nullable=False)