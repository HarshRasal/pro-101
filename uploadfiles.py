
import os
import shutil
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accesstoken)

        for root , dirs , files in os.walk(file_from):
            
            for filename in files:

                local_path = os.path.join(root,filename)

                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path , 'rb') as f:
                    dbx.files_upload(f,read(),dropbox_path,mode = WriteMode('overwrite'))


def main():
    access_token = ''
    transferdata = TransferData(access_token)

    file_from = input("the path of file to transfer")
    file_to = input("enter the full path of upload to dropbox")

    transferdata = upload_files(file_from,file_to)
    print("your file has been moved")