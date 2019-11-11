# Initialize GoogleDriveFile instance with file id.
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
# Create local webserver which automatically handles authentication.
gauth.LocalWebserverAuth()

# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)
# file_obj = drive.CreateFile({'id': '1wal3UGQFYYj1UcCBTDtvIy6auPkYHOou'})
# file_obj.GetContentFile('cats.png') # Download file as 'cats.png'.

file_list = drive.ListFile({'q': 'trashed=true', 'maxResults': 10}).GetList()
# file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
print(file_list)
for file1 in file_list:
    print(file1)
    print('title: %s, id: %s' % (file1['title'], file1['id']))
