import time
import os
import pyscreenshot as ImageGrab

def take_screenshot():            
    while True:        
        screenshot = ImageGrab.grab(bbox=(120,250,980,600))                                       
        screenshot.save('img.png')        
        print(f"Captured Frame!")                        
        time.sleep(2)

take_screenshot()