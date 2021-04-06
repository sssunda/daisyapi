import pytest
from app.main import create_app


@pytest.fixture(scope="session")
def client():
    app = create_app()

    with app.test_client() as client:
        # with app.app_context():
        #     init_db()
        yield client
