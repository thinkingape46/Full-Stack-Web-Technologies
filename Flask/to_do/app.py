from flask import Flask, render_template, url_for, redirect, jsonify, request
from bmi.forms import BmiCalculator
from python_scripts.bmi_calculator import bmi_calculator
from python_scripts.calculator import processing

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/bmi_page', methods=['GET', 'POST'])
def bmi_page():

    form = BmiCalculator()

    return render_template('bmi.html', form=form)

@app.route("/bmi")
def bmi():

    w = request.args.get("w", 1, type=int)
    h = request.args.get("h", 1, type=int)

    bmi = bmi_calculator(w, h)

    return jsonify(result = bmi)

@app.route("/calculator_page")
def calculator_page():
    return render_template('calculator.html')

@app.route("/calculator")
def calculator():

    calculator_input = request.args.get("a", "1", type=str)
    calculator_output = processing(list(calculator_input))

    print("result: {a}".format(a = calculator_output))
    return jsonify(result = calculator_output)



@app.route('/<name>')
def user_page(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)