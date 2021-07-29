from flask import Flask, Blueprint
from celery import Celery

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


def make_celery(app):
    celery = Celery(app.name,
                    backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['BROKER_URL'])
    celery.conf.update(app.config)
    return celery


app = create_app()
celery = make_celery(app)
