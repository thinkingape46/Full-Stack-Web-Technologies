# myproject/puppies/forms.py

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

# There is another add form inside the owners folder, but it will be taken care by blueprints.

class AddForm(FlaskForm):

    name = StringField('Name of the puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('Enter the id of the puppy:')
    submit = SubmitField('Remove Puppy')