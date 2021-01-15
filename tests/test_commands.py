from flapp.ext.db.commands import create_db, drop_db, populate_db


def test_create_db(app):
    assert create_db() == "Creates database"


def test_drop_db(app):
    assert drop_db() == "Cleans database"


def test_populate_db(app):
    assert len(populate_db()) == 3
