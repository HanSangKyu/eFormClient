__author__ = 'airkjh'

import requests

import auth
import property


class FormDAO:
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
        response = requests.post(url, data=payload)
        print response.text

    def get(self, formId):
        args = {
            'url': property.base_url + 'form/' + formId + '/get.json',
            'data': {
                'oauth_token': self.auth.getToken(),
                'workspace_id': property.workspace
            }
        }
        response = requests.post(**args)
        return response.json()['result']

    def echo(self):
        url = property.base_url + 'echo.json'
        payload = {
            'oauth_token': self.auth.getToken(),
            'workspace_id': property.workspace
        }
        response = requests.post(url, data=payload)
        print response.text


if __name__ == '__main__':
    form_client = FormDAO(auth.OAuth())
    #form_client.covers()
    print form_client.get('51b141fee4b00ab852adb44f')
    #form_client.echo()





