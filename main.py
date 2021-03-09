# PyAutoGUI lets Python control the mouse and keyboard,
# and other GUI automation tasks. For Windows, macOS,
# and Linux, on Python 3 and 2.
import pyautogui

# to take some break we need time
import time

# to make of our mouse point safe need to use pyautogui.FAILSAFE = False
pyautogui.FAILSAFE = False

# we use range here 5 to auto react for 5 posts
for i in range(0, 5):
    time.sleep(5)   # it will take 5 seconds beak
    pyautogui.press('j')   # j means timeline posts
    time.sleep(3)    # take 3 seconds break
    pyautogui.press('l')   # l for react
    time.sleep(3)   # take 3 seconds break
    pyautogui.press('tab')  # tab means take the love sign
    time.sleep(3)    # take 3 seconds break
    pyautogui.press('enter')   # press the enter to love react the post
