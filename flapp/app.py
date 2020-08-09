""" Main file """
from flask import Flask

from flapp.ext.config import settings as config


def create_app() -> Flask:
    """Create a Flask app

    Returns:
        Flask: Instance of Flask
    """
    app = Flask(__name__)

    config.init_app(app)
    return app
