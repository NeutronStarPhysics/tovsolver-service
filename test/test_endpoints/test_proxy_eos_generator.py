import uuid
import json
import pytest
from app import create_app

# python -m pytest -vhttps://serge-m.github.io/posts/testing-json-responses-in-flask-rest-apps-with-pytest/

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()


@pytest.fixture(scope='module')
def runner(app):
    return app.test_cli_runner()

def response_as_json(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')


def test_eos_generation_MIT(client):
    # Arrange
    payload = { 
        "name": str(uuid.uuid4()), 
        "type": "eos_generator", 
        "payload": { 
            "type": "mit_bag_model", 
            "rho_0": 100, 
            "bag_constant": 5 
            } 
        }


    response = post_json(client, '/invoke', payload)

    json_response = response_as_json(response)
    assert response.status_code == 201
    assert json_response["payload"] == payload["payload"]