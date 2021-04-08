from flask import current_app


def get_config(key):
    value = current_app.config.get(key)
    if value is None:
        raise ValueError
    return value
