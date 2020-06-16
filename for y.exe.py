import pyautogui
import time
from tkinter import *

time.sleep(2)
program_list = pyautogui.getAllTitles()
if 'Python' in program_list:
    print('not')