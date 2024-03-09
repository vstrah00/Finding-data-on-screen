import pyautogui

def image_location():
    try:
        # Attempt to locate the image on the screen
        res = pyautogui.locateOnScreen("ukupno.png", confidence=0.6)
        if res:
            print("Image found at:", res.left, res.top)
            return res
        else:
            return -1
    except pyautogui.ImageNotFoundException:
        return -2