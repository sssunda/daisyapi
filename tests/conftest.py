import sys
import pytest
import json
from app.main import create_app


@pytest.fixture(scope="session")
def client():
    app = create_app()

    with app.test_client() as client:
        # with app.app_context():
        #     init_db()
        yield client


def parse_body(resp):
    return json.loads(resp.data.decode("utf-8"))


# register custom function
sys.modules['pytest'].parse_body = parse_body
