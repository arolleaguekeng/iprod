import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import requests
from munch import DefaultMunch

from models.creations import Creation
from models.users import User


class Creationcontroller:
    def __int__(self):
        pass

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
                creation = DefaultMunch.fromDict(creation)
                datas.append(Creation(id=creation.id, name=creation.name, image=creation.image))
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
            creation = Creation(id=data.id, image=data.image,name=data.name)
            return creation
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))