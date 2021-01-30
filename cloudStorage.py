import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)


def main():
    access_token = 'sl.ApwotTgGhVJOEGEh01I-IC6gQkehY6pF6kX12dR5EkgxnOhMPD_5r3jH7JjiqBAPN8FxlkSSbJDC2vwRQtJBepA_p0EB1HBzdVKDsO0Jx5LZ1cneXD8MEPJZ8LpWXrruHFw7-xw'
    transferData = TransferData(access_token)

    file_from = input("Enter the file's path that you would like to upload ")
    file_to = input("Enter the path of dropbox to be uploaded")

    transferData.upload_file(file_from,file_to)
    print('File has been uploaded successfully')

main()
