from datetime import datetime
from task_manager import db, login_manager, bcrypt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# MODELS
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fullname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    joined_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    avatar = db.Column(db.String(40), default="avatar.png", nullable=False)
    user_note = db.relationship("Note", backref="userNote", lazy="dynamic")

    # Methods Used By flask login package to authenticate user periodically
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Method to verify password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="cascade"), nullable=False)
