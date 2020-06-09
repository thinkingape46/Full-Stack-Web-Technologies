# Import Flask class from flask

from flask import Flask

# creating an application object with the name "app" with the "__name__" variable.
# "__name__" is the python predefined variable which is set to the name of the module in which it is used.
app = Flask(__name__)

# add the route decorator, this links the page to the route, currently it is just ('/')
@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1><br><a href="about_me">About me</a><br>'


# Adding a second view
@app.route('/about_me')
def about():
    return '<h1>I am a Human</h1>'

# dynamic routing
# what greater than and less than symbols for?
@app.route('/<name>')
def dynamic(name):
    return f"The 100th character of name is {name[100]}"

# when debug mode = true, we get lot of information instead of just "internal server Error"
if __name__ == "__main__":
    app.run(debug=True)
