import pytest
import time
from flask import current_app
from app.api.auth.modules import encrypt


def _login(client, email, password):
    resp = client.post("/auth/login",
                       data={
                           "email": email,
                           "password": password
                       })
    assert resp.status_code == 200

    return pytest.parse_body(resp)["access_token"]


def test_verify_returns_200(client):
    email = 'test_user_1@test.com'
    password = 'password1'
    access_token = _login(client, email, password)
    resp = client.get("/auth/verify", headers={"Authorization": access_token})

    assert resp.status_code == 200


def test_verify_returns_400(client):
    # Does not have token
    resp = client.get("/auth/verify")

    assert resp.status_code == 400


def test_verify_returns_401_1(client):
    # It's not auth user
    email = 'test_user_3@test.com'
    access_token = encrypt.encrypt_jwt(email)
    resp = client.get("/auth/verify", headers={"Authorization": access_token})

    assert resp.status_code == 401


def test_verify_returns_401_2(client):
    # Access token has been expired
    email = 'test_user_1@test.com'
    password = 'password1'
    access_token = _login(client, email, password)
    time.sleep(current_app.config.get('JWT_EXP_PERIOD'))
    resp = client.get("/auth/verify", headers={"Authorization": access_token})

    assert resp.status_code == 401
