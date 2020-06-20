# myproject/owners/forms.py

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

# There is another add form inside the puppy folder, but it will be taken care by blueprints.
class AddForm(FlaskForm):

    name = StringField('Name of the owner:')
    id = IntegerField('id of the puppy:')
    submit = SubmitField('Submit')
