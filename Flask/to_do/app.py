from flask import Flask, render_template, url_for, redirect
from bmi.forms import BmiCalculator

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/bmi', methods=['GET', 'POST'])
def bmi_page():

    form = BmiCalculator()

    if form.validate_on_submit():

        weight = form.weight.data
        height = form.height.data

        bmi = (weight) / (height/100 * height/100)

        weight = 0

        return render_template('bmi.html', bmi=bmi, form=form)

    return render_template('bmi.html', form=form)

@app.route('/<name>')
def user_page(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)