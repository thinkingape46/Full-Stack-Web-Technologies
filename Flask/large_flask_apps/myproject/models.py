# Models.py
# setup db inside the __init__.py file under myproject folder.
from myproject import db

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):

        if self.owner:
            return "Puppy name is {a} (ID:{b}) and owner is {c}.".format(a=self.name, b=self.owner.owner_name, c=self.id)
        else:
            return "Puppy name is {a} (ID:{b}) and currently has no owner."

class Owner(db.Model):

    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, owner_name, puppy_id):
        self.owner_name = owner_name
        self.puppy_id = puppy_id
