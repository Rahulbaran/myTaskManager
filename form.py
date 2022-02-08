from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import EqualTo, DataRequired, ValidationError, Length
from wtforms.fields.simple import StringField, EmailField, PasswordField, SubmitField


# * SIGNUP FORM
class SignUpForm(FlaskForm):
    fullname = StringField(
        "Fullname",
        validators=[DataRequired(), Length(min=5, max=50, message="fullname should be 5 to 50 characters long")],
    )
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=5, max=50, message="username should be 5 to 30 characters long")],
    )
    email = EmailField(
        "Email",
        validators=[DataRequired(), Length(min=12, max=50, message="email should be 12 to 50 characters long")],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8, max=50, message="password should be 8 to 50 characters long")],
    )
    reenter_password = PasswordField(
        "Reenter Password", validators=[EqualTo("reentered password should match previous entered password")]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField("Signup")


# * LOGIN FORM
class LoginForm(FlaskForm):
    email = EmailField(
        "Email",
        validators=[DataRequired(), Length(min=12, max=50, message="email should be 12 to 50 characters long")],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8, max=50, message="password should be 8 to 50 characters long")],
    )
    submit = SubmitField("Login")
