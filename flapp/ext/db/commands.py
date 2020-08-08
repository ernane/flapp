from flapp.ext.db import db
from flapp.ext.db.models import Thing


def create_db():
    """Creates database"""
    db.create_all()
    return "Creates database"


def drop_db():
    """Cleans database"""
    db.drop_all()
    return "Cleans database"


def populate_db():
    """Populate db with sample data"""
    drop_db()
    create_db()

    data = [
        Thing(id=1, name="Thing A"),
        Thing(id=2, name="Thing B"),
        Thing(id=3, name="Thing C"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Thing.query.all()
