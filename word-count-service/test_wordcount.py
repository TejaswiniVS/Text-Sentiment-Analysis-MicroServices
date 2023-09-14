import pytest
import json
from wordcount import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_wordcount_valid_input(client):
    # Create a valid JSON payload with a 'text' field
    data = {'text': 'This is a test sentence.'}
    response = client.post('/count', json=data)

    assert response.status_code == 200
    assert json.loads(response.data) == {'result': 5}

def test_wordcount_missing_text_field(client):
    # Create a JSON payload missing the 'text' field
    data = {'other_field': 'Some value'}
    response = client.post('/count', json=data)

    assert response.status_code == 400
    assert json.loads(response.data) == {'error': 'Text field is missing in the JSON payload'}

def test_wordcount_exceeds_limit(client):
    # Create a JSON payload with text that exceeds the word count limit
    data = {'text': ' '.join(['word'] * 257)}  # 257 words
    response = client.post('/count', json=data)

    assert response.status_code == 400
    assert json.loads(response.data) == {'error': 'Word count exceeds the limit (256)'}

if __name__ == '__main__':
    pytest.main()