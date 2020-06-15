# Import Flask and render_template.
from flask import Flask, render_template

# Import FlaskForm with flask_wtf, this is for creating forms using flask instead of html.
from flask_wtf import FlaskForm

# Import the needed form fields, StringField for strings, we may always need a SubmitField
from wtforms import StringField, SubmitField


# Creating flask app
app = Flask(__name__)

# Configue a secret to have CSRF security work.
# app.config is a dictionary
app.config['SECRET_KEY'] = 'mysecretkey'

# Create an instance of WTF form.

class InfoForm(FlaskForm):

    # breed here is attribute of the class 'InfoForm'
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')

# Create a view and set methods 'GET' and 'POST'. GET are POST are for handling the forms.
@app.route('/', methods = ['GET', 'POST'])
def index():

    # Breed here is a variable.
    breed = False

    # Create an instance of the form.

    form = InfoForm()

    if form.validate_on_submit():

        breed = form.breed.data
        form.breed.data = ''

    return render_template('index.html', form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)
