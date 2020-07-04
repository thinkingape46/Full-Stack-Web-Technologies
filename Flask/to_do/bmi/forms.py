from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class BmiCalculator(FlaskForm):

    weight = IntegerField("Weight: ", validators=[DataRequired()])
    height = IntegerField("Height: ", validators=[DataRequired()])
    submit = SubmitField("Calculate BMI")