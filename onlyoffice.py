import requests
import urllib.parse
import json 
from config import config
from admincredentials import credentials

class OnlyOfficeAuthenticator:
    def __init__(self):
        self.admin_authkey = self.getAuthenticationToken(credentials['admin_login'],credentials['admin_password'])

    def registerUser(self, name, email, password):
        headers = {
            'Authorization': self.admin_authkey,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        data = {
            'firstname': name,
            'lastname': ' ',
            'email': email,
            'password': password[0:30],
        }
        try:
            response = requests.post(
                f"{config['onlyofficeUrl']}/api/2.0/people.json?filtervalue={email}",
                headers=headers,
                data=data,
            )
            print(response)
            if response.status_code == 401:
                self.admin_authkey = self.getAuthenticationToken(credentials['admin_login'],credentials['admin_password'])

        except:
            print('failed to register user')


    def getAuthenticationToken(self, email, password):
        response = requests.post(f"{config['onlyofficeUrl']}/api/2.0/authentication.json", json={'userName': email, 'password':password[0:30]}).json()
        print(response)
        if response['statusCode'] != 201:
            return 'failed boo'
        return response['response']['token']

