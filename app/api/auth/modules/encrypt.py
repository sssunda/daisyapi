import jwt
import time
from flask import current_app


def _get_config(key):
    value = current_app.config.get(key)
    if value is None:
        raise ValueError
    return value


def _validate_jwt(data):
    for key in ["email", "iat", "exp"]:
        if key not in data:
            raise KeyError


def encrypt_jwt(email):
    jwt_exp_period = _get_config("JWT_EXP_PERIOD")
    jwt_algo = _get_config("JWT_ALGO")
    jwt_secret_key = _get_config("JWT_SECRET_KEY")

    iat = time.time()
    payload = {"email": email, "iat": iat, "exp": iat + jwt_exp_period}
    return jwt.encode(payload, jwt_secret_key, algorithm=jwt_algo)


def decrypt_jwt(token):
    data = jwt.decode(token,
                      _get_config("JWT_SECRET_KEY"),
                      algorithms=[_get_config("JWT_ALGO")])
    _validate_jwt(data)
    return data
