"""
Entity Recognition API Documentation

This Flask application provides a simple API that identifies and classifies named entities (e.g., persons, organizations, locations) in the text.

Usage:
- Send a POST request to '/entity' with a JSON payload containing a 'text' field to classify.

Endpoints:
- POST /entity: classify the entities in text.

"""
from flask import Flask, request, jsonify

app = Flask(__name__)

"""
Here actual etity recognition is not applied,returns a hardcoded JSON response:
 {
        "text": "Apple Inc.",
        "label": "ORG"
        }
This endpoint allows clients to send a POST request with a JSON payload containing a 'text' field. 
Returns:
JSON: A JSON response containing the hardcoded result.
"""
@app.route('/entity', methods=['POST'])
def entityrecognition():
    try:
        data = request.get_json()
        text = data.get('text')
        if text is None:
            return jsonify({"error": "Text field is missing in the JSON payload"}), 400
        result = [{
        "text": "Apple Inc.",
        "label": "ORG"
        }]
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8003, debug=True)