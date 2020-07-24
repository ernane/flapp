import pytest

from flapp.app import create_app


@pytest.fixture
def app():
    """Instance of Main flask app"""
    return create_app()
