import os
from pathlib import Path
for folderName, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        a= os.path.getsize(os.path.join(folderName,filename))
        if a>100000000:
            print(filename, "is of size ", a//100000000, "MB with path: ", os.path.join(folderName,filename))
            