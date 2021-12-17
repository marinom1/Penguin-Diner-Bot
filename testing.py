import pyautogui
import win32api
win32api.SetCursorPos((836, 229))
from pytesseract import pytesseract
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("Pixel checking:",pyautogui.pixel(836, 229))

#print(pyautogui.pixel(1559, 356) == (220, 236, 239))

print(pyautogui.pixel(838, 229) == (16, 18, 15) or (13,16,14))

