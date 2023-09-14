from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    text = data.get('text')
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        sentiment = "positive" 
    elif blob.sentiment.polarity < 0:
        sentiment = "negative" 
    else:
        sentiment = "neutral"

    return jsonify({"result": sentiment}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)
