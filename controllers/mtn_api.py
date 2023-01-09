import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import requests
import sys


class PaiementMoMo:
    def __init__(self, phone_number, amound):
        self.content_type = 'application/json'
        self.x_reference_id = '80d310f2-fe7d-4f3c-9e3a-184b49a29935'
        self.ocp_Apim_subscription_Key = 'a2b909d218e1477ba010515c92562a47'
        self.x_target_environment = 'sandbox'
        self.phone_number = phone_number
        self.amound = amound


    # Authanticate User
    def authenticate_user(self):
        headers = {
            # Request headers
            'X-Reference-Id': self.x_reference_id,
            'Content-Type': self.content_type,
            'Ocp-Apim-Subscription-Key': self.ocp_Apim_subscription_Key
        }

        body = {"providerCallbackHost": "google.com"}

        try:
            response = requests.post("https://sandbox.momodeveloper.mtn.com/v1_0/apiuser?", headers=headers,
                                     data=json.dumps(body))
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # generate Api Key
    def generate_api_key(self):
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': self.ocp_Apim_subscription_Key,
        }
        params = urllib.parse.urlencode({
        })
        try:
            conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
            conn.request("POST", "/v1_0/apiuser/{}/apikey?%s".format(self.x_reference_id) % params, "{body}", headers)
            response = conn.getresponse()
            key = response.read()
            key = key.decode("utf-8")
            key = json.loads(key)
            key = key['apiKey']
            key = base64.b64encode('{}:{}'.format(self.x_reference_id, key).encode('utf-8'))
            key = 'Basic {}'.format(key.decode("utf-8"))
            conn.close()
            return key
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


    # get Tokent
    def get_token(self, key):
        headers = {
            # Request headers
            'Authorization': key,
            'Ocp-Apim-Subscription-Key': self.ocp_Apim_subscription_Key,
        }

        params = urllib.parse.urlencode({
        })
        try:
            conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
            conn.request("POST", "/collection/token/?%s" % params, "", headers)
            response = conn.getresponse()
            resp_dict = response.read()
            resp_dict = resp_dict.decode("utf-8")
            resp_dict = json.loads(resp_dict)
            access_token = resp_dict['access_token']
            conn.close()
            return access_token
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


    # Start transaction
    def requesttopay(self,
                     currency='EUR',
                     externalId='1234',
                     country_code='237',
                     partyIdType='MSISDN',
                     payerMessage='string',
                     payeeNote='string', ):
        self.authenticate_user()
        key = self.generate_api_key()
        access_token = self.get_token(key)
        access_token = 'Bearer {}'.format(access_token)
        headers = {
            # Request headers
            'Authorization': access_token,
            'X-Reference-Id': self.x_reference_id,
            'X-Target-Environment': self.x_target_environment,
            'Content-Type': self.content_type,
            'Ocp-Apim-Subscription-Key': self.ocp_Apim_subscription_Key,
        }

        body = {
            "amount": self.amound,
            "currency": currency,
            "externalId": externalId,
            "payer": {
                "partyIdType": partyIdType,
                "partyId": country_code + self.phone_number
            },
            "payerMessage": payerMessage,
            "payeeNote": payeeNote,
        }

        try:
            response = requests.post("https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay?",
                                     headers=headers,
                                     data=json.dumps(body))
            print(response.json())
            return response.status_code
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
