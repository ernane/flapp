import os


def init_app(app):
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["FLASK_ADMIN_SWATCH"] = "simplex"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI", "sqlite://")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILER_ENABLED"] = True
