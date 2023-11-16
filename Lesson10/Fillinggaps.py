import os
import re

ask1 = input('prefix of file: ')
extension = input('enter extension: ')
folder = input('absolute path of the folder: ')

files = []

for file in os.listdir(folder):
    if file.endswith(extension):
        req = re.compile(fr'({ask1}\d\d\d)')
        mo = req.findall(file)
        for i in mo:
            files.append(i)
##Stuck
