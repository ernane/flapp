from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flapp.ext.db import db
from flapp.ext.db.models import Thing

admin = Admin()


def init_app(app):
    admin.name = app.config.get("FLASK_ADMIN_NAME", "Flapp - Prod")
    admin.template_mode = app.config.get("FLASK_ADMIN_TEMPLATE_MODE", "bootstrap3")
    admin.add_view(ModelView(Thing, db.session))

    admin.init_app(app)
