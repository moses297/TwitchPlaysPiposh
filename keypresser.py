import pyautogui
from time import sleep

class Keypresser:
    def one_mouse_click(self, x):
        pyautogui.moveTo(x)
        pyautogui.click()

    def two_mouse_click(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        sleep(0.1)
        pyautogui.click()
