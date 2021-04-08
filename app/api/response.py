from flask import make_response
import json
import datetime


def success(data: dict = {}, msg="", status_code=200):
    assert isinstance(data, dict)

    data["timestamp"] = datetime.datetime.now().isoformat()
    data["message"] = msg

    return make_response(json.dumps(data), status_code)
