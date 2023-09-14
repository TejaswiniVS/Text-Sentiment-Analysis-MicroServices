"""
Sentiment Analysis API Documentation

This Flask application provides an API for sentiment analysis of text using TextBlob.

Usage:
- Send a POST request to '/sentiment' with a JSON payload containing a 'text' field to analyze text sentiment.

Endpoints:
- POST /sentiment: Analyze the sentiment of the provided text.

"""
from flask import Flask, jsonify, request
from textblob import TextBlob

app = Flask(__name__)

"""
    Analyze the sentiment of the provided text.

    This endpoint allows clients to send a POST request with a JSON payload containing a 'text' field. 
    The API will perform sentiment analysis on the provided text using TextBlob and return the sentiment result.

    Returns:
        JSON: A JSON response containing the sentiment analysis result.
"""
@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    try:
        data = request.get_json()
        text = data.get('text')

        if not text:
            return jsonify({"error": "Missing 'text' in request data"}), 400
        
        blob = TextBlob(text)

        sentiment = polarity_check(blob.sentiment.polarity)
        
        return jsonify({"result": sentiment}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to check the polarity of the text
def polarity_check(polarity):
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment

# Start the Flask app when this script is executed.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)
