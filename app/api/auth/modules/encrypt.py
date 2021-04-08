import jwt
import time
from app.configs import get_config


def encrypt_jwt(email):
    jwt_exp_period = get_config('JWT_EXP_PERIOD')
    jwt_algo = get_config('JWT_ALGO')
    jwt_secret_key = get_config('JWT_SECRET_KEY')

    iat = time.time()
    payload = {'email': email, 'iat': iat, 'exp': iat + jwt_exp_period}
    return jwt.encode(payload, jwt_secret_key, algorithm=jwt_algo)
