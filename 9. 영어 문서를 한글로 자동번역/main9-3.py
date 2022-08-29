import os

import googletrans

translator = googletrans.Translator()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

read_file_path = '영어파일.txt'

with open(read_file_path, 'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
