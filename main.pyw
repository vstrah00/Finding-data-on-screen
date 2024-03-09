import pyautogui
import numpy
import pytesseract
import cv2
import PIL.Image
import time
import keyboard
import sys
from screenshot import screenshot_func
from read_from_image import read_from_image_func

def detect_sequence():
    sequence = []

    # Define a callback for key events
    def on_key_event(event):
        nonlocal sequence

        # Append the name of the pressed key to the sequence list
        sequence.append(event.name)

        # Check if the sequence contains 'esc' followed by 'enter'
        if sequence[-2:] == ['esc', 'enter']:
            sequence.clear()  # Clear the sequence to start scanning again
            if screenshot_func() < 0:
                print("Error taking a screenshot")
            else:    
                receipt_value = read_from_image_func()
                print(receipt_value)

    # Register the callback for key events
    keyboard.on_press(on_key_event)

    # Keep the program running until 'esc' is pressed
    while True:
        time.sleep(0.1)  # Add a small delay to reduce CPU usage
        if keyboard.is_pressed('alt'):
            sys.exit(0)
            break  # Exit the loop if 'alt' is pressed

    # Unregister the callback to avoid memory leaks
    keyboard.unhook_all()

# Call the function to start detecting the sequence
detect_sequence()
