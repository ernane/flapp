""" Main file """
from flask import Flask

from flapp.ext import admin, cli, config, db, site, toolbar


def create_app() -> Flask:
    """Create a Flask app

    Returns:
        Flask: Instance of Flask
    """
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    site.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    admin.init_app(app)
    return app
