import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# step 1: Setup SQLite database
# basedir gives the path of the file i.e basic.py
# abspath is the absolute path.
basedir = os.path.abspath(os.path.dirname(__file__))

# Step 2: Create a flask application.

app = Flask(__name__)

# Step 3: Connect he flask application to the database.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
# If want to track the modification, for now it is False to make things simple.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# SQL database is set.

# Create a first model. inherited from db.mode.
# Model is just setting up a table in the database.
# 
class Puppy(db.Model):
    # a default table will be provided, if you want to overwrite it.
    # Name will be of your choice, and shall replace the default value.
    __tablename__ = 'puppies'

    # Creat a column for the table.
    # Creata a attribute 'id' and setting it to a column inside the table.
    # primate key is the unique identifier for the key. let's assume we have lot of puppies, if we have puppies with the same name inside the table. 
    # So, one column will be a primary identifier, id is unique. so first puppy will have a id of 1, second of 2 and so on.. 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    # Setup a init method.

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # We dont need an id, it will be auto-created for us.

    # This method gives the string representation fo the object.
    def __repr__(self):
        return 'Puppy {a} is {b} year old.'.format(a=self.name, b=self.age)