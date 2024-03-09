import pytesseract
import PIL.Image

myconfig= r"--psm 8 --oem 3"

def read_from_image_func():
    text = pytesseract.image_to_string(PIL.Image.open("screenshot.png"), config=myconfig)
    num=float(text)
    return num