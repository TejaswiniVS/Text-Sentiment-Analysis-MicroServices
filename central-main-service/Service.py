import json

class Service:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        with open('services.json', 'r') as file:
            return json.load(file)

    def get(self, name: str, field: str):
        for uuid, values in self.data.items():
            if values.get('name') == name:
                return values.get(field)

    def get_uuid(self, name: str):
        return self.get(name, 'id')

    def get_url(self, name: str):
        return self.get(name, 'url')

    def get_port(self, name: str):
        return self.get(name, 'port')
