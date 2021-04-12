from flask import request
import time

from app.api import response
from app.api.auth.database import TEST_USER
from app.api.auth.modules.encrypt import decrypt_jwt


def jwt_token_required(func):
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token is None:
            return response.bad_request()

        try:
            decoded_token = decrypt_jwt(token)

        except KeyError:
            return response.unauthorized("Invalid token give")

        auth_user = TEST_USER.get(decoded_token["email"])
        if auth_user is None:
            return response.unauthorized("Invalid token given")

        exp = decoded_token["exp"]
        if exp < time.time():
            return response.unauthorized("Access token has been expired")

        kwargs["auth_email"] = decoded_token["email"]
        kwargs["jwt_exp"] = exp
        kwargs["jwt_iat"] = decoded_token["iat"]
        return func(*args, **kwargs)

    return decorated_function
