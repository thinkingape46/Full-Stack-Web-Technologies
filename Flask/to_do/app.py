from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/info')
def info():
    return render_template('info.html')
    

@app.route('/<name>')
def user_page(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)