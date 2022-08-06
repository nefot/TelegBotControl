import pyautogui


def Make_Photo():
    image = pyautogui.screenshot()
    image.save(r'pic.png')
