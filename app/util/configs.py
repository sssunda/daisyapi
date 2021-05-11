from flask import current_app as app


def get_config(key):
    value = app.config.get(key)
    if value is None:
        raise ValueError
    return value
