import pytest


def _login(client, email, password):
    resp = client.post("/auth/login",
                       data={
                           "email": email,
                           "password": password
                       })
    assert resp.status_code == 200

    return pytest.parse_body(resp)["access_token"]


def test_send_return_200(client):
    email = 'test_user_1@test.com'
    password = 'password1'
    access_token = _login(client, email, password)
    resp = client.post('/mail',
                       data={
                           'subject': 'TEST임',
                           'to_addrs': [
                               'sundaeun93@gmail.com',
                           ],
                           'body': 'TEST중~~~~'
                       },
                       headers={'Authorization': access_token})

    assert resp.status_code == 200


def test_send_return_404_1(client):
    # no body in data
    resp = client.post('/mail/send',
                       data={'to_mail_address': 'sundaeun93@gmail.com'})

    assert resp.status_code == 404


def test_send_return_404_2(client):
    # no destination address in data
    resp = client.post('/mail/send',
                       data={
                           'to_mail_address': '',
                           'body': 'TEST!'
                       })

    assert resp.status_code == 404
