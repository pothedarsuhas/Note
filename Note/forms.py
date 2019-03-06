from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, TextAreaField, PasswordField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, ValidationError, url

from .models import user

class LoginForm(FlaskForm):
    email = StringField("Your Email: ", validators=[DataRequired()])
    password = PasswordField('Your Password: ', validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField()

class AddNoteForm(FlaskForm):
    title = StringField("Title: ", validators=[DataRequired()])
    content = TextAreaField("Content: ", validators=[DataRequired()])

class SignupForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(),Length(3,25)])
    password = PasswordField("Password", validators=[DataRequired(), Length(8,25)]) #, EqualTo(password, message='passwords must match')
    password2 = PasswordField("Password: ", validators=[DataRequired(), Length(8,25) ])
    email = StringField('Email: ', validators=[DataRequired(), Email(), Length(2,25)])

    def validate_email(self, email):
        if (user.query.filter_by(email = email.data).first()):
            raise ValidationError("This email id already exists.")

    def validate_username(self, username):
        if (user.query.filter_by(username = username.data).first()):
            raise ValidationError("This username already exists.")

