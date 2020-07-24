""" Main file """
from flask import Flask

from flapp.ext import commands, config, site, toolbar, admin


def create_app() -> Flask:
    """Create a Flask app

    Returns:
        Flask: Instance of Flask
    """
    app = Flask(__name__)

    config.init_app(app)
    site.init_app(app)
    commands.init_app(app)
    toolbar.init_app(app)
    admin.init_app(app)
    return app
