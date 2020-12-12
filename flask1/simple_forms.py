from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, email_validator, ValidationError
from flask1.models import Doctor


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = StringField('Password', validators=[DataRequired()])
    remember_pass = BooleanField('Remember Me')
    submit = SubmitField('Login')
