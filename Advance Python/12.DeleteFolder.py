import os
if os.path.exists("D:/Python Advance/new"):
    os.rmdir("D:/Python Advance/new")
    print('folder deleted')
else:
    print('Folder does not deleted')