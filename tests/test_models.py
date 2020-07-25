"""Model unit tests."""
from flapp.ext.db.models import Thing

# from .factories import ThingFactory


def test_get_by_id(db):
    """Get thing by ID."""
    thing = Thing(id=1, name="Thing A")
    db.session.add(thing)
    db.session.commit()

    retrieved = Thing.query.get(thing.id)
    assert retrieved == thing
    assert repr(retrieved) == "<Thing 'Thing A'>"
