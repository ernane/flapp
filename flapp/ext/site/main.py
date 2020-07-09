from flask import Blueprint, render_template

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("base.html", page="Index")


@bp.route("/home")
def home():
    return render_template("base.html", page="Home")
