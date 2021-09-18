from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Initializing application

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    app.secret_key = 'password'

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app