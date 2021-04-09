import pytest

_EMAIL = 'test_user_1@test.com'
_PASSWORD = 'password1'


def _login(client):
    resp = client.post("/auth/login",
                       data={
                           "email": _EMAIL,
                           "password": _PASSWORD
                       })
    assert resp.status_code == 200

    return pytest.parse_body(resp)["access_token"]


def test_me_returns_200(client):
    access_token = _login(client)
    resp = client.get("/auth/me", headers={"Authorization": access_token})

    assert resp.status_code == 200

    data = pytest.parse_body(resp)
    assert data["email"] == _EMAIL
