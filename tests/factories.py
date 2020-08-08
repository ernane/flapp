"""Factories to help in tests."""
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from flapp.ext.db import db
from flapp.ext.db.models import Thing


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class ThingFactory(BaseFactory):
    """Thing factory."""

    name = Sequence(lambda n: f"thing{n}")

    class Meta:
        """Factory configuration."""

        model = Thing
