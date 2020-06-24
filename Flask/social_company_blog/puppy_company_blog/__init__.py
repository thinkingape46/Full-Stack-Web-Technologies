# puppy_company_blog/__init__.py

from flask import Flask

app = Flask(__name__)

from puppy_company_blog.core.views import core
from puppy_company_blog.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)