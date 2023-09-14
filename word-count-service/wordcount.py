"""
Word Count API Documentation

This Flask application provides a simple API for counting the number of words in a text.

Usage:
- Send a POST request to '/count' with a JSON payload containing a 'text' field to get the word count.

Endpoints:
- POST /count: Count the words in the provided text.

"""
from flask import Flask, request, jsonify

app = Flask(__name__)
"""
Count the number of words in the provided text.
This endpoint allows clients to send a POST request with a JSON payload containing a 'text' field. 
The API will count the number of words in the provided text and return the result in a JSON response.
Returns:
JSON: A JSON response containing the word count result.
"""


@app.route('/count', methods=['POST'])
def wordcount():
    try:
        data = request.get_json()
        text = data.get('text')

        if text is None:
            return jsonify({"error": "Text field is missing in the JSON payload"}), 400

        count = len(text.split())

        # if word count is more than 256 then throw a bad request exception.
        # This is done to test error handling between microservices.
        # In production environment, there could be many such exceptions and cases.
        if count > 256:
            return jsonify({"error": "Word count exceeds the limit (256)"}), 400

        return jsonify({"result": count}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8002, debug=True)
