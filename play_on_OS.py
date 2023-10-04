import pyautogui
import os
import time

song = input("Enter the name of the song and artist(optional): ")
print("Song is " + song)
time.sleep(2)
os.system("spotify")
print("Please wait. . . . .")
time.sleep(6)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write(song, interval=0.1)

for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
    time.sleep(1)
    pyautogui.press(key)