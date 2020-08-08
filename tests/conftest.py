import pytest

from flapp.app import create_app
from flapp.ext.db import db as _db


@pytest.fixture
def app():
    """Instance of Main flask app"""
    return create_app()


@pytest.fixture
def db(app):
    """Create database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()
