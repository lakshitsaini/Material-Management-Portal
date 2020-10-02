from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file1 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": "1d7SPfSL1bQRicIpZWRc5EY_WaotFBF8r"}]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentFile(file_name)

file1.Upload()
