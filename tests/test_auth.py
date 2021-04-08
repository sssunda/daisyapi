def test_auth(client):
    resp = client.get("/auth/")
    assert resp.status_code == 200
