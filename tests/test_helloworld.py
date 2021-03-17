def test_helloworld(client):
    resp = client.get("/hello")
    assert resp.status_code == 200
    assert resp.data == b'Hello, World!'
