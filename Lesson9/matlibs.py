import os
from pathlib import Path

forbidden = ['adjective', 'noun', 'adverb', 'verb']

file_path = '/home/bot2.0/Documents/Automate-the-boring-Stuff-with-Python/Lesson9/library.txt'
with open(file_path, 'r') as f:
    words = f.read().split()

for index, word in enumerate(words):
    if word.lower() in forbidden:
        ask = input(f"Enter a replacement for '{word}': ")
        words[index] = ask

with open(file_path, 'w') as f1:
    f1.write(' '.join(words))
