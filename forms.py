"""
User Forms using Flask Extension

- Write python class that will be automatically converted into html forms

"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # enable filling form

# allow us to put constraints on StringFields
from wtforms.validators import DataRequired, Length, Email, EqualTo

# create registration form inheriting from FlaskForm


class RegistrationForm(FlaskForm):
    username = StringField('Username',  # label of stringfields
                           validators=[DataRequired(),  # cannot be empty
                                       Length(min=2, max=20)])  # no. of chars
    email = StringField('Email',
                        validators=[DataRequired(),  # cannot be empty
                                    Email()])  # must have email format

    password = PasswordField('Password',
                             validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('Password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    # login with email is ezier to remember
    email = StringField('Email',
                        validators=[DataRequired(),  # cannot be empty
                                    Email()])  # must have email format

    password = PasswordField('Password',
                             validators=[DataRequired()])

    submit = SubmitField('Sign Up')
