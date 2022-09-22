import os
if os.path.exists("D:/Python Advance/new/text3.txt"):
    os.remove("D:/Python Advance/new/text3.txt")
    print('file deleted')
else:
    print('this file does not exists')