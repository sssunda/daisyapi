from flask_restx import Resource, reqparse
from flask import request

from app.api import response
from app.api.restx import api
from app.api.auth.database import TEST_USER
from app.api.auth.modules.encrypt import encrypt_jwt, encrypt_password, decrypt_jwt
from app.api.auth.modules.decorate import jwt_token_required

ns = api.namespace("auth", description="Endpoints for user auth")

parser = reqparse.RequestParser()
parser.add_argument("email", required=True)
parser.add_argument("password", required=True)


@ns.route("/login")
class Login(Resource):
    def post(self):
        parsed = parser.parse_args()

        password = TEST_USER.get(parsed.email)
        if password is None or password != encrypt_password(parsed.password):
            # Invalid email or password
            return response.bad_request()

        access_token = encrypt_jwt(parsed.email)
        return response.success({"access_token": access_token})


@ns.route("/verify")
class Verify(Resource):
    @jwt_token_required
    def get(self, **kwargs):
        return response.success(msg="Token has been verified")


@ns.route("/whoami")
class WhoAmI(Resource):
    def get(self):
        response_data = dict()
        response_data['REMOTE_ADDR'] = request.remote_addr
        response_data['HTTP_USER_AGENT'] = request.environ.get('HTTP_USER_AGENT')
        response_data['QUERY_STRING'] = request.query_string.decode('utf-8')
        request_authorization = request.environ.get('HTTP_AUTHORIZATION')

        if (request_authorization):
            user_data = decrypt_jwt(request_authorization)
            response_data['user_email'] = user_data['email']
            response_data['jwt_exp'] = (user_data['exp'] - user_data['iat']) / 60

        return response.success(response_data)
