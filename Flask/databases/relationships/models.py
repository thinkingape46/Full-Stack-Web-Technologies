# Imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # One to many relation.
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')

    # One to one relationship.
    # uselist=False, because unlike toys, each puppy has only one owner.
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # if puppy has owner:
        if self.owner:
            return "Puppy is {a} and owner is {c}.".format(a=self.name, c=self.owner.owner_name)
        
        else:
            return "Puppy is {a} and has no owner yet.".format(a=self.name)

    def report_toys(self):
        print("I have the following toys")
        for toy in self.toys:
            print(toy.item_name)

class Toy(db.Model):
    
    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):

    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.Text)

    # Connect the owner to the puppy.
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, owner_name, puppy_id):
        self.owner_name = owner_name
        self.puppy_id = puppy_id
