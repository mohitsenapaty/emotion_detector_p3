from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os



def create_subfolder(folder,sfldname):
    new_folder = drive.CreateFile({'title':'{}'.format(sfldname),'mimeType':'application/vnd.google-apps.folder'})
    if folder is not None:
        new_folder['parents'] = [{u'id': folder['id']}]
    new_folder.Upload()
    return new_folder
    
def root_files():    
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    # Auto-iterate through all files in the root folder.
    #for file1 in file_list:
    #    print 'title: %s, id: %s' % (file1['title'], file1['id'])
    return file_list    
    
def upload_files_to_folder(fnames, folder):
    #file1 = drive.CreateFile({'title': 'Hello.txt'}) # Create GoogleDriveFile instance with title 'Hello.txt'
    #file1.Upload() # Upload it
    #print 'title: %s, id: %s' % (file1['title'], file1['id']) # title: Hello.txt, id: {{FILE_ID}}
    
    for fname in fnames: 
        nfile = drive.CreateFile({'title':os.path.basename(fname),
                                  'parents':[{u'id': folder['id']}]})
        nfile.SetContentFile(fname)
        nfile.Upload() 
        
def list_files_with_ext(ext,dir='./'):
    return sorted(filter(lambda f:f[-len(ext):]==ext,os.listdir(dir)))
    

def find_folders(fldname):
    file_list = drive.ListFile({
        'q': "title='{}' and mimeType contains 'application/vnd.google-apps.folder' and trashed=false".format(fldname)
        }).GetList()
    return file_list    

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth) 

#file1 = drive.CreateFile({'title': 'ip.txt'})
#file1.Upload() # Upload the file.
import pdb; pdb.set_trace()



