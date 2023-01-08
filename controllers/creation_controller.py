import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import requests
from munch import DefaultMunch

from models.creations import Creation
from models.users import User


class Creationcontroller:
    def __int__(self):
        pass

    def map_json_to_creation(self, json_responce):
        creation = DefaultMunch.fromDict(json_responce)
        creation = Creation(id=creation.id,
                            name=creation.name,
                            image=creation.image,
                            amound=creation.amound,
                            created_at=creation.created_at,
                            description=creation.descriptions)
        return creation

    def get_all(self):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
        }

        try:
            response = requests.get("http://127.0.0.1:8000/api/get-all-creations", headers=headers)
            data = response.json()
            print(data)
            datas = []
            for creation in data:
                creation = self.map_json_to_creation(creation)
                datas.append(creation)
            return datas
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def get_by_id(self, id):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
        }

        try:
            response = requests.get("http://127.0.0.1:8000/api/get-creation/{}".format(id), headers=headers)
            data = response.json()
            print(data)
            data = DefaultMunch.fromDict(data)
            creation = self.map_json_to_creation(data)
            return creation
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def edit_creation(self, creation: Creation):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
        }

        body = {
            "name": creation.name,
            "image": creation.image,
            "descriptions": creation.description,
            "amound": creation.amound,
            "created_at": creation.created_at
        }

        try:
            response = requests.put("http://127.0.0.1:8000/api/edit-creation/{}/".format(creation.id),
                                    headers=headers,
                                    data=json.dumps(body))
            print('{}|{}'.format(response.status_code, response.json()))
        except Exception as e:
            print("{}".format(e))
