from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
# for multi-line import, use paranthesis.
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField, 
                    RadioField, SelectField, TextAreaField, TextField)

# import validators
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

# Create a form class.
class InfoForm(FlaskForm):

    # What's inside the paranthesis is a 'label' like the one in HTML.
    # We can add validators inside paranthesis. By default, the validators are none.
    # Validators are a list of validator objects.
    breed = StringField('What breed are you:', validators=[DataRequired()])

    neutered = BooleanField('Are you neutered?')
    mood = RadioField('Please choose your mood:', choices=[('mood_one', 'Happy'),('mood_two','Excited')])

    food_choice = SelectField(u'Pick your favourite food', choices=[('chi', 'Chicken'), ('fish', 'Fish')])

    feedback = TextAreaField('Please enter your feedback:')
    submit = SubmitField('Submit')

# Create a view
@app.route('/', methods=['GET', 'POST'])
def index():
    
    form = InfoForm()
    if form.validate_on_submit():

        # Use of session object. unlike cookies, sessions are not permanenlty saved.
        # Data is stored for only this session.
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        # return for the inf statement
        return redirect(url_for('thankyou'))

    # return for the function 'def index()'
    return render_template('index.html', form = form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
