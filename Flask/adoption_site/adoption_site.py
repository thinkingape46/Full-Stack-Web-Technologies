# import os
import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm, AddOwnerForm

# create a flask app
app = Flask(__name__)

# Setup a secret for our forms.
app.config['SECRET_KEY'] = 'mysecretkey'

###################### SQL DATABASES ###########################

basedir = os.path.abspath(os.path.dirname(__file__))

# join base directory with 'data.sqlite'                                            
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a databse by passing application into SQLAlchemy
db = SQLAlchemy(app)
# Giving the ability to migrate.
Migrate(app, db)

# Creat a model puppy:

class Puppy(db.Model):

    # change the table name

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name    

    def __repr__(self):
        if self.owner:
            return "Puppy name is {a} (id:{c}) and owner is {b}.".format(a=self.name, b=self.owner.owner_name, c=self.id)
        else:
            return "Puppy name is {a} and currenly has no owner".format(a=self.name)

class Owner(db.Model):

    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.Text)

    # Connect the owner to the puppy model.
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, owner_name, puppy_id):
        self.owner_name = owner_name
        self.puppy_id = puppy_id


# View functions.

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_puppy', methods=['GET', 'POST'])
def add_puppy():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_puppy = Puppy(name)
        db.session.add(new_puppy)
        db.session.commit()
        return redirect(url_for('list_puppy'))

    return render_template('add.html', form=form)

@app.route('/del_puppy', methods=['GET', 'POST'])
def del_puppy():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        # Get the name of the puppy.
        puppy = Puppy.query.get(id)

        db.session.delete(puppy)
        db.session.commit()
        
        return redirect(url_for('list_puppy'))

    return render_template('delete.html', form=form)

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    # instantiate AddOwnerForm class.
    form = AddOwnerForm()

    if form.validate_on_submit():
        id = form.pup_id.data
        # puppy = Puppy.query.get(id)
        name = form.name.data
        new_owner = Owner(name, id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_puppy'))
    
    return render_template('add_owner.html', form=form)


@app.route('/list_puppies')
def list_puppy():

    puppies = Puppy.query.all()

    return render_template('list.html', puppies=puppies)


if __name__ == '__main__':
    app.run(debug=True)