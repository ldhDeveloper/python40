import pyautogui
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('pic1.PNG')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic2.PNG')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic3.PNG')
    print(picPosition)