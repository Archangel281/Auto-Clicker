import time
import pyautogui

def move_curser():
    pyautogui.click()

time.sleep(3)
start_time = time.time()
current_time = time.time()

while current_time - start_time < 10:
    move_curser()
    current_time = time.time()
