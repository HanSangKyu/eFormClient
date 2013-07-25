import requests

import auth
import property


class Resource:
    auth

    def __init__(self, auth):
        self.auth = auth

    def covers(self):
        url = property.base_url + 'form/covers.json'
        payload = {
            'oauth_token': self.auth.getToken(),
            'workspace_id': property.workspace,
            'start': 0,
            'limit': 100
        }
        response = requests.post(url, payload)
        print response.text


if __name__ == '__main__':
    form_client = Resource(auth.OAuth())
    form_client.covers()
