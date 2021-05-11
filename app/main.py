from flask import Flask, Blueprint

from app.api.auth.api import ns as ns_auth
from app.api.mail.api import ns as ns_mail
from app.api.restx import api


def create_app():
    app = Flask(__name__)

    # config setting
    app.config.from_pyfile("./configs/dev.py")

    blueprint = Blueprint("api", __name__)
    api.init_app(blueprint)
    api.add_namespace(ns_auth)
    api.add_namespace(ns_mail)

    app.register_blueprint(blueprint)
    return app


app = create_app()
