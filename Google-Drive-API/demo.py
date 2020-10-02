from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

fileId = ''
def upload(filename):

    file1 = drive.CreateFile({'title' : filename,"parents": [{"kind": "drive#fileLink", "id": "1d7SPfSL1bQRicIpZWRc5EY_WaotFBF8r"}]})
    file1.SetContentFile('../Files/' + filename)
    # print('Uploaded!')
    file1.Upload()
    global fileId
    fileId = file1['id']

def getfile(id):
	source = drive.CreateFile({'id': id})
	return source

def delete(id):
    file = getfile(id)
    file.Delete()
