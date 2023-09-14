import pytest
from recognitionservice import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_entityrecognition_successful(client):
    data = {'text': 'Apple is a technology company.'}
    response = client.post('/entity', json=data)

    assert response.status_code == 200
    result = response.json
    assert 'result' in result
    entities = result['result']
    assert len(entities) == 1
    entity = entities[0]
    assert 'text' in entity
    assert entity['text'] == 'Apple Inc.'
    assert 'label' in entity
    assert entity['label'] == 'ORG'

def test_missing_text_field(client):
    data = {}  # Missing 'text' field
    response = client.post('/entity', json=data)

    assert response.status_code == 400
    error = response.json
    assert 'error' in error
    assert 'Text field is missing in the JSON payload' in error['error']

if __name__ == '__main__':
    pytest.main()