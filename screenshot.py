import cv2
import pyautogui
import numpy
from locate_on_screen import image_location


def screenshot_func():
    location = image_location()
    if isinstance(location, int):
        return -1
    else:
        image1 = pyautogui.screenshot(region=(int(location.left)+370, int(location.top), 100, 50))
        image1 = cv2.cvtColor(numpy.array(image1), cv2.COLOR_RGB2BGR)
        cv2.imwrite("screenshot.png", image1)
        return 0