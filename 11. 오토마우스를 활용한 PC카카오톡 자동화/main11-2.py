import pyautogui
import pyperclip
import time
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

clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

pyperclip.copy("이 메시지는 자동으로 보내지는 메세지 입니다~~")
pyautogui.hotkey("ctrl", "v")
time.sleep(1.0)

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)