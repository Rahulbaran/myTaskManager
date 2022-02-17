from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import EqualTo, DataRequired, ValidationError, Length
from wtforms.fields.simple import StringField, EmailField, PasswordField, SubmitField, BooleanField, TextAreaField
from .models import User


# * SIGNUP FORM
class SignUpForm(FlaskForm):
    fullname = StringField(
        "Fullname",
        validators=[DataRequired(), Length(min=5, max=50, message="fullname should be 5 to 50 characters long")],
    )
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=5, max=20, message="username should be 5 to 20 characters long")],
    )
    email = EmailField(
        "Email",
        validators=[DataRequired(), Length(min=12, max=50, message="email should be 12 to 50 characters long")],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8, max=30, message="password should be 8 to 30 characters long")],
    )
    reenter_password = PasswordField(
        "Reenter Password",
        validators=[EqualTo("password", message="reentered password should match with password")],
    )
    recaptcha = RecaptchaField()
    submit = SubmitField("Signup")

    # * Custom Validators
    def validate_password(self, password):
        specialCharacters = "!@#$%^&*()_-+=|\\}{][:;?/>.<,~`\"'"
        totalSpecialChar = 0
        for char in password.data:
            if char in specialCharacters:
                totalSpecialChar += 1
        if totalSpecialChar == 0:
            raise ValidationError("password should contain atleast one special character")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("username is already taken")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("email is already taken")


# * LOGIN FORM
class LoginForm(FlaskForm):
    email = EmailField(
        "Email",
        validators=[DataRequired(), Length(min=12, max=50, message="email should be 12 to 50 characters long")],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8, max=30, message="password should be 8 to 30 characters long")],
    )
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

    # * Custom Validators
    def validate_password(self, password):
        specialCharacters = "!@#$%^&*()_-+=|\\}{][:;?/>.<,~`\"'"
        totalSpecialChar = 0
        for char in password.data:
            if char in specialCharacters:
                totalSpecialChar += 1
        if totalSpecialChar == 0:
            raise ValidationError("password should contain atleast one special character")
