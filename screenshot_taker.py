import numpy as np
import cv2
import pyautogui
import os
import time 

count = 0
condition = True
print("Welcome to Screenshot program")
infinite_loop_or_not = input("Do you want to take a screenshot every specific time (y/n) : ")
if infinite_loop_or_not.lower() == "y":
    condition = True
    time_of_timer = int(input("For how long (seconds) : "))
else:
    condition = False
    
while True:
    count += 1
    # take screenshot using pyautogui
    image = pyautogui.screenshot()

    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # create directory if it doesn't exist
    directory = r"D:\screenshots"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # save image in the specified directory
    file_name = "screenshot_" + time.strftime('%Y%m%d-%H%M%S') + ".png"
    file_path = os.path.join(directory, file_name)
    cv2.imwrite(file_path, image)

    print(f"screenshot({count}) has been taken")
    
    if not condition:
        break
    else:
        time.sleep(time_of_timer)
