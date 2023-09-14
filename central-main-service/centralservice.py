from flask import Flask, request, jsonify
import requests, json
import os.path
from Service import Service
import uuid

app = Flask(__name__)

registered_services = {}

# Configuration
JSON_FILE_PATH = 'services.json'

if os.path.exists(JSON_FILE_PATH):
    try:
        with open(JSON_FILE_PATH, 'r') as json_file:
            registered_services = json.load(json_file)
    except Exception as e:
        print(f"Error loading JSON file: {str(e)}")
        registered_services = {}
else:
    registered_services = {}

@app.route('/services', methods=['POST'])
def register_service():
    data = request.get_json()
    service_id = str(uuid.uuid4())
    new_service = Service
    new_service.id = service_id
    new_service.name= data.get('name')
    new_service.port= data.get('port')
    new_service.url= data.get('url')

    if new_service.name in [service['name'] for service in registered_services.values()]:
        return jsonify({"message": "Service already exists"}), 400        

    registered_services[service_id] = { "name": new_service.name, "port":new_service.port, "url": new_service.url }

    with open(JSON_FILE_PATH,'w') as service_file:
        json.dump(registered_services, service_file, indent=4)
    return jsonify({"message": "Service registered successfully"}), 200


@app.route('/services', methods=['GET'])
def list_services():
    return jsonify(registered_services), 200

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    service_name = str(data.get('service'))
    text = data.get('text')

    if service_name not in [service['name'] for service in registered_services.values()]:
         return jsonify({"error": "Requested service does not exist"}), 404
    
    new_service = Service()
    service_url = new_service.get_url(service_name)

    response = requests.post(service_url, json={"text": text})

    if response.status_code != 200:
        return jsonify({"error": "Service request failed"}), 500
    
    result = response.json()
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)