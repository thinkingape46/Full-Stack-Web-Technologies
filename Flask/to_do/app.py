from flask import Flask, render_template, url_for, redirect, jsonify, request
from bmi.forms import BmiCalculator

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route("/bmi")
def bmi():

    w = request.args.get("w", 1, type=int)
    h = request.args.get("h", 1, type=int)
    bmi = w / (h/100 * h/100) 

    return jsonify(result = bmi)


@app.route('/bmi_page', methods=['GET', 'POST'])
def bmi_page():

    form = BmiCalculator()

    return render_template('bmi.html', form=form)

@app.route('/<name>')
def user_page(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)