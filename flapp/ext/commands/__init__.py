from .main import init


def init_app(app):
    for command in [init]:
        app.cli.add_command(command)
