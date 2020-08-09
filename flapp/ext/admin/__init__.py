from flask_admin import Admin

admin = Admin()


def init_app(app):
    admin.name = app.config.get("FLASK_ADMIN_NAME", "Flapp")
    admin.template_mode = app.config.get("FLASK_ADMIN_TEMPLATE_MODE", "bootstrap3")
    admin.init_app(app)
