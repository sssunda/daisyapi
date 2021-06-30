import pytest
import json


def _login(client, email, password):
    resp = client.post("/auth/login",
                       data={
                           "email": email,
                           "password": password
                       })
    assert resp.status_code == 200

    return pytest.parse_body(resp)["access_token"]


def test_whoami_returns_200_1(client):
    email = 'test_user_1@test.com'
    password = 'password1'
    access_token = _login(client, email, password)
    resp = client.get("/auth/whoami?p=par&&t=too",
                      headers={
                          "Authorization": access_token,
                      },
                      json={'test': 'TTTT', 't': 'T'}
                      )

    assert resp.status_code == 200


def test_whoami_returns_200_2(client):
    resp = client.get("/auth/whoami?next=/test/")
    resp_data = json.loads(resp.data.decode('utf-8'))

    assert resp.status_code == 200

    assert resp_data['QUERY_STRING'] == "next=/test/"
