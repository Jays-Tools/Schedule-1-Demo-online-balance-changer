import pyperclip
import pyautogui
import tkinter as tk
import time
# Hello! if you don't Know how python works etc..DO NOT CHANGE ANYTHING IN HERE! OR IT WILL NOT WORK!
time.sleep(1)

text = """{
    "DataType": "MoneyData",
    "DataVersion": 0,
    "GameVersion": "0.2.9f4",
    "OnlineBalance": 580000.5,
    "Networth": 580000.5
}"""

pyperclip.copy(text)

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("appdata", interval=0.1)
pyautogui.press("enter")
time.sleep(1)

pyautogui.write("local")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("TVGS")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("schedule I")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("Saves")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("SaveGame_1")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("Money")
pyautogui.press("enter")

time.sleep(1)

pyautogui.hotkey("ctrl", "A")
pyautogui.press("backspace")
time.sleep(1)

pyautogui.hotkey("ctrl", "V")

time.sleep(1)

pyautogui.hotkey("ctrl", "S")

time.sleep(2)

pyautogui.write("Money.json")

time.sleep(1)

pyautogui.press("enter")

time.sleep(1)

pyautogui.press("left")

time.sleep(1)

pyautogui.press("enter")

time.sleep(1)

pyautogui.hotkey("alt", "F4")

time.sleep(1)