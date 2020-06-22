# myproject/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Creating an instance of LoginManager
login_manager = LoginManager()

# Creating an app
app = Flask(__name__)

# Make configurations

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create our database.
db = SQLAlchemy(app)
Migrate(app, db)

# Pass app in to login manager. 
# Take in 'login_manager' we have created under imports, and call the 'init_app' from the object.
# pass in the app
login_manager.init_app(app)

# configuring the view for the login.
login_manager.login_view = 'login'