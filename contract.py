import time
import requests
import auth
import property


class Contract:
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

    def registerChapter(self, folderId, file_path, prop):
        url = property.base_url + 'chapter/' + folderId + '/upload.json'
        default_payload = {
            'oauth_token': self.auth.getToken(),
            'workspace_id': property.workspace,
            'originalResourceId': '51b53a32e4b02710b90614ee',
            'resourceOrder': 1,
            'lastModified': '1373864180280'
        }
        _payload = default_payload.copy()
        _payload.update(prop)

        file = {'file': open(file_path, 'rb')}
        resp = requests.post(url, data=_payload, files=file)
        return resp.json()


if __name__ == '__main__':
    contract = Contract(auth.OAuth())
    prop = {
        'prop1': 'value1',
        'prop2': 'value2',
        'prop3': 'value3',
        'prop4': 'value4'

    }
    contractRoot = '51e5019ee4b09407e4ddf782'
    formId = '51b141fee4b00ab852adb44f'
    title = 'cde1234_' + str(int(time.time()))
    seq = ''
    file_path = '/Users/airkjh/Downloads/test.jpg'

    respDict = contract.open(contractRoot, formId, title, seq)
    print respDict

    chapterFolderId = respDict['chapters']

    print contract.registerChapter(folderId=chapterFolderId, file_path=file_path, prop=prop)


