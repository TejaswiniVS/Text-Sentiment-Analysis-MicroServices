from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/count', methods=['POST'])
def wordcount():
    data = request.get_json()
    text = data.get('text')
    count = len(text.split())
    return jsonify({"result": count}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8002, debug=True)