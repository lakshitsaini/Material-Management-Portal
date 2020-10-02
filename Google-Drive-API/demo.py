from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

def upload(filename):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    file1 = drive.CreateFile('title':filename,{"parents": [{"kind": "drive#fileLink", "id": "1d7SPfSL1bQRicIpZWRc5EY_WaotFBF8r"}]})
    file1.SetContentFile('../Files/' + filename)

    file1.Upload()
