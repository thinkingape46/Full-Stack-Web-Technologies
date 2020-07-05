from flask import Flask, render_template, url_for, redirect, jsonify, request
from bmi.forms import BmiCalculator
from python_scripts.bmi_calculator import bmi_calculator

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

    a = request.args.get("a", "1", type=str)
    print("result: {a}".format(a = a))
    return jsonify(result = list(a))



@app.route('/<name>')
def user_page(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)