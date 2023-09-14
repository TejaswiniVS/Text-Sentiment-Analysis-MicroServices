"""
Flask Application Documentation

This Flask application provides a simple service registration and analysis platform.

Usage:
- Register services via POST request to /services.
- List registered services via GET request to /services.
- Analyze text using registered services via POST request to /analyze.

Author: [Tejaswini Sadegaonkar]
Date: [09/13/2023]

"""

from flask import Flask, render_template, request, jsonify
import requests, json
import os.path
from Service import Service
import uuid

app = Flask(__name__)

registered_services = {}

# Registered services are stored in services.json JSON file
JSON_FILE_PATH = 'services.json'

# Loads the services.json file into registered_services when the application is started
if os.path.exists(JSON_FILE_PATH):
    try:
        with open(JSON_FILE_PATH, 'r') as json_file:
            registered_services = json.load(json_file)
    except Exception as e:
        print(f"Error loading JSON file: {str(e)}")
        registered_services = {}
else:
    registered_services = {}


@app.route('/')
def home():
    return

# Registers services
@app.route('/services', methods=['POST'])
def register_service():
    try:
        data = request.get_json()
        service_id = str(uuid.uuid4())
        new_service = Service
        new_service.id = service_id
        new_service.name= data.get('name')
        new_service.port= data.get('port')
        new_service.url= data.get('url')
        # Checks if service with same name is present,if yes returns error message
        if new_service.name in [service['name'] for service in registered_services.values()]:
            return jsonify({"message": "Service already exists"}), 400        

        registered_services[service_id] = { "name": new_service.name, "port":new_service.port, "url": new_service.url }

        with open(JSON_FILE_PATH,'w') as service_file:
            json.dump(registered_services, service_file, indent=4)

        return jsonify({"message": "Service registered successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Lists all the services registered
@app.route('/services', methods=['GET'])
def list_services():
    try:
        return jsonify(registered_services), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Performs text analysis,calls the particular service based on service name
@app.route('/analyze', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json()
        service_name = str(data.get('service'))
        text = data.get('text')

        if service_name not in [service['name'] for service in registered_services.values()]:
             return jsonify({"error": "Requested service does not exist"}), 404
    
        new_service = Service()
        service_url = new_service.get_url(service_name)
        # Calls the respective service
        response = requests.post(service_url, json={"text": text})

        if response.status_code != 200:
            return jsonify({"error": "Service request failed"}), 500
    
        result = response.json()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask app when this script is executed.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)