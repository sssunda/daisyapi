def test_login_returns_200(client):
    resp = client.post("/auth/login",
                       data={
                           "email": "test_user_1@test.com",
                           "password": "password1"
                       })
    assert resp.status_code == 200


def test_login_returns_400(client):
    resp = client.post("/auth/login",
                       data={
                           "email": "test_user_1@test.com",
                           "password": "password2"
                       })
    assert resp.status_code == 400
