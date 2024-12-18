import pytest
# test/__init__.py
import sys
sys.path.append('/vagrant/test_pytest/mypkg')
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data
