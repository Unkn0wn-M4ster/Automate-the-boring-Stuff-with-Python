import os
import shutil

home_path = '/home/bot2.0/Documents/Automate-the-boring-Stuff-with-Python'
newpath = os.path.join(home_path, 'newfolder')

try:
    os.mkdir(newpath)
except FileExistsError:
    print(f"The folder '{newpath}' already exists.")

extension = input('Input file type: ')

try:
    for folderName, subfolders, filenames in os.walk(home_path):
        for filename in filenames:
            if filename.endswith(extension):
                source_path = os.path.join(folderName, filename)
                shutil.copy(source_path, newpath)
                print(f"Copying: {source_path} to {newpath}")

except:
    print('no files with said extension')