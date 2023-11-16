import re
import os

ask = input("Enter expression to be checked: ")
req = re.compile(ask)

try:
    for filename in os.listdir():
        if filename.endswith('.txt'):
            with open(filename, 'r') as f:
                words = f.read()
                find = req.findall(words)
                if find:
                    print(f"File {filename} has expression \"{ask}\"")
except :
    print('NO EXPRESSION MATCHED')
