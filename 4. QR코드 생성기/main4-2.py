import os
import qrcode

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = 'qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF-8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)
        save_path = qr_data + '.png'
        qr_img.save(save_path)
