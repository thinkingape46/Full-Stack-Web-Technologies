# import class Flask and render_template from flask

from flask import Flask, render_template

# Create an app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("basic.html")

if __name__ == "__main__":
    app.run(debug=True)