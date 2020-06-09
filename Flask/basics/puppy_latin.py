# import class Flask
from flask import Flask

# Creation of app
app = Flask(__name__)

# Creating of first view
@app.route('/')
def index():
    return "<h1>This is the Home Page</h1><br><a href='puppy_latin'>Click here to go to Puppy Latin page</a>"

# Creation of view for Puppy Latin

@app.route('/puppy_latin')
def pup_lat_home():
    return "<h1>This is the Home Page for PuppyLatin<br>Go to /puppy_latin/name</h1><br><a href='/'>Go to Home Page</a>"

# Creating of dynamic view
@app.route('/puppy_latin/<name>')
def pup_lat(name):

    p_l = name

    if p_l[-1] != "y":
        p_l = p_l + "y"
        return "The Puppy Latin translation for {a} is {b}<br><a href='/'>Go to Home Page</a>".format(a = name, b = p_l)
    
    elif p_l[-1] == "y":
        
        part_zero = p_l[:-1]
        part_one = "iful"
        p_l = part_zero + part_one
        return "The Puppy Latin translation for {a} is {b}<br><a href='/'>Go to Home Page</a>".format(a = name, b = p_l)

if __name__ == "__main__":
    app.run(debug=True)