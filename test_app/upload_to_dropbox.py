import dropbox
DROPBOX_ACCESS_TOKEN = "t0-WvXEmgaAAAAAAAAAABkLheYrQk8TjSZBJHBgkn1nQ3X0K6z0H-P_zABFzFY9E"

class upload_to_dropbox:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file_v1(self, file_from=None, file_to=None):
        """upload a file to Dropbox using API v1
        """
        # Construct a DropboxClient instance
        client = dropbox.client.DropboxClient(self.access_token)

        with open(file_from, 'rb') as f:
            response = client.put_file(file_to, f)

    def upload_file(self, file_from=None, file_to=None):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        #files_upload(f, path, mode=WriteMode('add', None), autorename=False, client_modified=None, mute=False)
        #dbx.users_get_current_account()
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

        shared_link_metadata = dbx.sharing_create_shared_link_with_settings(file_to)
        self.shared_url = shared_link_metadata.url
        #print shared_link_metadata.url

    def get_shared_file_url(self):
        return self.shared_url

def main():
    transferData = upload_to_dropbox(DROPBOX_ACCESS_TOKEN)

    file_from = '../un2attention_data_2017_08_09_02_11_24.png'
    file_to = '/dharna_app/un2attention_data_2017_08_09_02_11_24.png'    # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from=file_from, file_to=file_to)
    print (transferData.get_shared_file_url())

if __name__ == '__main__':
    main()

