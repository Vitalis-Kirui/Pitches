from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initializing application
app = Flask(__name__, instance_relative_config=True)
# default value during development
app.secret_key = 'password'
# overridden if this file exists in the instance folder
app.config.from_pyfile('config.py', silent=True)

# Setting up configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views
from app import  errors