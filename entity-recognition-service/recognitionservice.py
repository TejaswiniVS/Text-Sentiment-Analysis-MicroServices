from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/entity', methods=['POST'])
def entityrecognition():
    data = request.get_json()
    text = data.get('text')
    result = [{
    "text": "Apple Inc.",
    "label": "ORG"
    }]
    return jsonify({"result": result}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8003, debug=True)