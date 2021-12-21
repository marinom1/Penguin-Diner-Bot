import pyautogui
import win32api
# win32api.SetCursorPos((1485, 229))
from pytesseract import pytesseract
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("Pixel checking:",pyautogui.pixel(1485, 229))

#print(pyautogui.pixel(1559, 356) == (220, 236, 239))


