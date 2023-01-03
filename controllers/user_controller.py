import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import requests
from munch import DefaultMunch


class Usercontroller:
    def __int__(self):
        pass

    # Authanticate User
    def authenticate_user(self,username,password):

        try:
            data = self.get_all()
            for user in data:
                user = DefaultMunch.fromDict(user)
                if user.email == username and user.password == password:
                    return True
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    def get_all(self):
        headers = {
            # Request headers
            'Content-Type': 'application/json',
        }

        try:
            response = requests.get("http://127.0.0.1:8000/api/get-all-users", headers=headers)
            data = response.json()
            return data
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))