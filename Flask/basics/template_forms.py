from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/puppy_band')
def puppy_band():
    return render_template('puppy_signup.html')

@app.route('/')
def index():
    return render_template('puppy_band.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('fn')
    last = request.args.get('ln')
    return render_template('signup_thank_you.html', first=first, last=last)

# @app.route('/<typo_word>')
# def error_page(typo_word):
#     if typo_word not in ["puppy_band", "thank_you"]:
#         return render_template('error.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)