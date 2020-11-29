from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, email_validator, ValidationError
from flask1.models import Doctor


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = Doctor.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username exists')

    def validate_email(self, email):
        user = Doctor.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email exists')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[DataRequired()])
    remember_pass = BooleanField('Remember Me')
    submit = SubmitField('Login')
