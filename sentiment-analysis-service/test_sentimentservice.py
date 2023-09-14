import pytest
import json
from sentimentservice import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_sentiment_analysis_positive(client):
    data = {'text': 'Today is great!'}
    response = client.post('/sentiment', json=data)

    assert response.status_code == 200
    result = response.json
    assert result['result'] == 'positive'

def test_sentiment_analysis_negative(client):
    data = {'text': 'I feel sad.'}
    response = client.post('/sentiment', json=data)

    assert response.status_code == 200
    result = response.json
    assert result['result'] == 'negative'

def test_sentiment_analysis_neutral(client):
    data = {'text': 'The weather is blah.'}
    response = client.post('/sentiment', json=data)

    assert response.status_code == 200
    result = response.json
    assert result['result'] == 'neutral'

def test_missing_text_field(client):
    data = {}  # Missing 'text' field
    response = client.post('/sentiment', json=data)

    assert response.status_code == 400
    error = response.json
    assert 'error' in error
    assert 'Missing \'text\' in request data' in error['error']

if __name__ == '__main__':
    pytest.main()