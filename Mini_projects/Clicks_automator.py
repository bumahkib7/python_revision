import pyautogui as pyautogui

myClicks = pyautogui.locateOnScreen('clicks.png', confidence=0.9)
print(myClicks)
pyautogui.click(myClicks)
