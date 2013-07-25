__author__ = 'airkjh'

import requests

import auth
import property


class Form:
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
                'workspace_id': property.workspace,
            }
        }
        response = requests.post(**args)
        print response.text


if __name__ == '__main__':
    form_client = Form(auth.OAuth())
    #form_client.covers()
    form_client.get('51ec9481e4b0abcef8eaec95')


