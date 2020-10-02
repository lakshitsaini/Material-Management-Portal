from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'Hello.txt',"parents": [{"kind": "drive#fileLink", "id": "1d7SPfSL1bQRicIpZWRc5EY_WaotFBF8r"}]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Hello World!') # Set content of the file from given string.
file1.Upload()
