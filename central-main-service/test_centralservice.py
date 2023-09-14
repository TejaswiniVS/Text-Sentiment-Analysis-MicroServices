import pytest
import json
from centralservice import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register_service(client):
    # Test registering a new service
    data = {'name': 'TestService', 'port': 8080, 'url': 'http://localhost:8080'}
    response = client.post('/services', json=data)

    assert response.status_code == 200
    assert json.loads(response.data) == {"message": "Service registered successfully"}

def test_list_services(client):
    # Test listing registered services
    response = client.get('/services')

    assert response.status_code == 200
    services = json.loads(response.data)
    assert isinstance(services, dict)
    assert 'TestService' in [service['name'] for service in services.values()] # Assuming you registered 'TestService' in a previous test

def test_analyze_text(client):
    # Assuming 'TestService' has been registered
    registered_services = client.get('/services').get_json()
    assert 'TestService' in [service['name'] for service in registered_services.values()]

    # Test text analysis using a registered service
    data = {'service': 'word-count', 'text': 'This is a test text.'}
    response = client.post('/analyze', json=data)

    assert response.status_code == 200
    result = json.loads(response.data)
    assert 'result' in result

def test_register_service_present(client):
    # Assuming 'TestService' has been registered
    # Test Registering a already present service
    data = {'name': 'TestService', 'port': 8080, 'url': 'http://localhost:8080'}
    response = client.post('/services', json=data)

    assert response.status_code == 400
    assert json.loads(response.data) == {"message": "Service already exists"}

if __name__ == '__main__':
    pytest.main()