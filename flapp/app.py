from flask import Flask
from flapp.ext import site, commands


def create_app():
    app = Flask(__name__)

    site.init_app(app)
    commands.init_app(app)
    return app
