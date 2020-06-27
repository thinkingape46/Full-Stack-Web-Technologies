from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
# This import will allow users to update their profile picture. 
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppy_company_blog.models import User

class LoginForm(FlaskForm):

    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):

    email = StringField('Email: ', validators=[DataRequired(), Email()])
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match')])
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])
    
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This Email has been already registered!')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("This Username has been already taken")

    submit = SubmitField('Register')

class UpdateUserForm(FlaskForm):

    email = StringField("Email: ", validators=[DataRequired(), Email()])
    username = StringField("Username: ", validators=[DataRequired()])
    picture = FileField("Update profile picture", validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This Email has been already registered.')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("This Username has been already taken")
        