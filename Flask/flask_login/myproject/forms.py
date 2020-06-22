from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from myproject.models import User

class LoginForm(FlaskForm):

    email = StringField(label='Email:', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    log_in = SubmitField(label='Log In')

class RegistrationForm(FlaskForm):
    
    # DataRequired() makes sure that field is filled.
    # EqualTo() checks if the certain fields are given the same input.
    # 'label' is what shown to the user.
    email = StringField(label='Email:', validators=[DataRequired(), Email()])
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Password must match!')])
    pass_confirm = PasswordField(label='Confirm Password', validators=[DataRequired()])
    register = SubmitField(label='Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email has been already registered')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username has been already registered')
