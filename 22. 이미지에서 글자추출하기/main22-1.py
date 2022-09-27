from PIL import Image
import pytesseract
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

image_path = "한글이미지.png"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(image_path), lang="kor")

print(text)