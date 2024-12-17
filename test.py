import pytest
from app import app


@pytest.fixture
def client():
    # Configure the Flask app for testing
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_is_working(client):
    # Send a GET request to the root URL
    response = client.get('/')
    
    # Assert the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert the response data contains the expected text
    assert b"Hello World!" in response.data

