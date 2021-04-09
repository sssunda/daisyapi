from flask_restx import Resource, reqparse

from app import TEST_USER
from app.api.restx import api
from app.api.auth.modules.encrypt import encrypt_jwt
from app.api import response
from app.api.auth.modules.decorate import jwt_token_required

ns = api.namespace("auth", description="Endpoints for user auth")

parser = reqparse.RequestParser()
parser.add_argument("email", required=True)
parser.add_argument("password", required=True)


@ns.route("/")
class Auth(Resource):
    def get(self):
        return 'hello'


@ns.route("/login")
class Login(Resource):
    def post(self):
        parsed = parser.parse_args()

        password = TEST_USER.get(parsed.email)
        if password is None or password != parsed.password:
            # Invalid email or password
            return response.bad_request()

        access_token = encrypt_jwt(parsed.email)
        return response.success({"access_token": access_token})


@ns.route("/me")
class Me(Resource):
    @jwt_token_required
    def get(self, **kwargs):
        return response.success({"email": kwargs["auth_email"]})
