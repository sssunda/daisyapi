from flask import make_response
import json
from datetime import datetime


def success(data: dict = {}, msg="", status=200):
    assert isinstance(data, dict)

    data["timestamp"] = datetime.now().isoformat()
    data["message"] = msg

    return make_response(json.dumps(data), status)


def bad_request(msg="Bad request"):
    return error(msg=msg, status=400)


def unauthorized(msg="Unauthorized"):
    return error(msg=msg, status=401)


def invalid_param_error(msg="Invalid parameter error"):
    return error(msg=msg, status=422)


def error(msg="System error", status=500):
    return make_response(
        json.dumps({
            "meesage": msg,
            "timestamp": datetime.now().isoformat()
        }), status)
