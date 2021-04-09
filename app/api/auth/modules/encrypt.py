import jwt
import time
from app.configs import get_config


def __validate_jwt(data):
    for key in ["email", "iat", "exp"]:
        if key not in data:
            raise KeyError


def encrypt_jwt(email):
    jwt_exp_period = get_config("JWT_EXP_PERIOD")
    jwt_algo = get_config("JWT_ALGO")
    jwt_secret_key = get_config("JWT_SECRET_KEY")

    iat = time.time()
    payload = {"email": email, "iat": iat, "exp": iat + jwt_exp_period}
    return jwt.encode(payload, jwt_secret_key, algorithm=jwt_algo)


def decrypt_jwt(token):
    data = jwt.decode(token,
                      get_config("JWT_SECRET_KEY"),
                      algorithms=[get_config("JWT_ALGO")])
    __validate_jwt(data)
    return data
