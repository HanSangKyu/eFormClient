import time
import requests
import auth
import property


class ContractDAO:
    auth

    def __init__(self, auth):
        self.auth = auth

    def open(self, folderId, formId, title, sequence):
        url = property.base_url + 'contract/create.json'
        payload = {
            'oauth_token': self.auth.getToken(),
            'workspace_id': property.workspace,
            'userId': '@eformui',
            'folderId': folderId,
            'formId': formId,
            'title': title,
            'sequence': sequence
        }
        resp = requests.post(url, data=payload)
        return resp.json()['contractFolders']

    def registerChapter(self, folderId, file_path, org_resource_id, last_modified, prop):
        url = property.base_url + 'chapter/' + folderId + '/upload.json'
        default_payload = {
            'oauth_token': self.auth.getToken(),
            'workspace_id': property.workspace,
            'originalResourceId': org_resource_id,
            'resourceOrder': 1,
            'lastModified': last_modified
        }
        _payload = default_payload.copy()
        _payload.update(prop)

        file = {'file': open(file_path, 'rb')}
        resp = requests.post(url, data=_payload, files=file)
        return resp.json()

    def get(self, contract_id):
        url = property.module_url + 'contract/' + contract_id + '/get.json'
        payloads = {
            'oauth_token': self.auth.getToken(),
            'workspace_id': property.workspace
        }
        return requests.post(url, data=payloads)

    def registerAttachment(self, folderId, file_path):
        url = property.base_url + 'attachment/' + folderId + '/upload.json'
        payload = {
            'oauth_token': self.auth.getToken(),
            'workspace_id': property.workspace
        }
        file = {'file': open(file_path, 'rb')}
        resp = requests.post(url=url, data=payload, files=file)

        return resp.json()


if __name__ == '__main__':
    pass
