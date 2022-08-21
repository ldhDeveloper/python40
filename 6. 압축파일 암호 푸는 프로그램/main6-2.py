import itertools
import zipfile
import os

passwd_string = "01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '암호1234.zip'

zFile = zipfile.ZipFile(file_path)

for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd=passwd.encode())
            print(f"비밀번호는 {passwd} 입니다")
            break
        except:
            pass
