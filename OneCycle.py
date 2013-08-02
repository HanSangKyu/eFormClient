__author__ = 'airkjh'

import time

from auth import OAuth
from formDAO import FormDAO
from contractDAO import ContractDAO


if __name__ == "__main__":
    _auth = OAuth()
    _formDAO = FormDAO(_auth)
    _contractDAO = ContractDAO(_auth)

    _formId = "51b141fee4b00ab852adb44f"

    form = _formDAO.get(_formId)
    _title = form['name'] + "_pyclient_" + str(int(time.time()))

    resource = form['resources'][0]
    controls = resource['controls']

    props = {}

    for control in controls:
        props[control['fieldId']] = control['fieldId'] + '_value'

    folders = _contractDAO.open(folderId=_auth.user['contractRootId'], formId=_formId, title=_title, sequence="")
    chapterFolderId = folders['chapters']
    attachment_id = folders['attachments']

    print 'chapterFolderId = ', chapterFolderId
    print 'attachment_id = ', attachment_id
    print 'prop = ', props
    print 'org_resource_id = ', resource['id']
    print 'last_modified=', resource['touch']

    _contractDAO.registerChapter(folderId=chapterFolderId,
                                 file_path="/Users/airkjh/Desktop/Mercedes_Benz_05.jpg",
                                 prop=props,
                                 org_resource_id=resource['id'],
                                 last_modified=resource['touch'])

    print _contractDAO.registerAttachment(folderId=attachment_id,
                                          file_path='/Users/airkjh/Desktop/attachments.jpg')
