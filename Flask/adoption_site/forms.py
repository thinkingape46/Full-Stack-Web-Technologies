from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of the Puppy:')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField("Id number of Puppy to remove:")
    submit = SubmitField('Remove Puppy')

class AddOwnerForm(FlaskForm):
    name = StringField("Name of the Owner:")
    pup_id = IntegerField("Id of the Puppy:")
    submit = SubmitField("Add Owner")