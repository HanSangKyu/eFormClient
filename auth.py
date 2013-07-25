__author__ = 'airkjh'

import requests
import property


class OAuth:
    user = {}
    oauthToken = {
        'oauthToken': '',
        'refreshToken': '',
        'expiresIn': ''
    }

    def getToken(self):
        if self.oauthToken['oauthToken'] == '':
            self.login()

        return self.oauthToken['oauthToken']

    def login(self):
        url = property.auth_url + 'login.json'
        payload = {
            'userId': property.auth_id,
            'passwd': property.auth_pwd,
            'workspaceId': property.workspace
        }
        response = requests.post(url, params=payload)
        json = response.json()



        token = json['token']
        user = json['user']

        self.oauthToken['oauthToken'] = token['oAuthToken']
        self.oauthToken['refreshToken'] = token['refreshToken']
        self.oauthToken['expiresIn'] = token['expiresIn']
        self.user = user


if __name__ == '__main__':
    oauth = OAuth()
    oauth.login()


