from flask import Flask
import json
import pytest

from handlers.routes import configure_routes


@pytest.fixture
def app():
    app = Flask(__name__)
    configure_routes(app)

    yield app

def test_base_route(app):
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Heipparallaa!'
    assert response.status_code == 200