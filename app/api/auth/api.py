from flask_restx import Resource

from app.api.restx import api

ns = api.namespace("auth", description="Endpoints for user auth")


@ns.route("/")
class Auth(Resource):
    def get(self):
        return 'hello'
