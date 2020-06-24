# puppy_company_blog/__init__.py

from flask import Flask

app = Flask(__name__)

from puppy_company_blog.core.views import core

app.register_blueprint(core)