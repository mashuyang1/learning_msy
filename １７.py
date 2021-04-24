import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('识别图片.png'))
text2 = pytesseract.image_to_string((Image.open('code.jpg')))
pic = pytesseract.image_to_string((Image.open('img.png')))
print(pic)
