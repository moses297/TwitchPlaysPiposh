from time import sleep

import pyautogui


class Keypresser:

    @staticmethod
    def one_mouse_click(x):
        pyautogui.moveTo(x)
        pyautogui.click()

    @staticmethod
    def two_mouse_click(x):
        pyautogui.moveTo(x)
        pyautogui.click()
        sleep(0.1)
        pyautogui.click()

    @staticmethod
    def triple_click_300():
        pyautogui.moveTo((300, 300))
        pyautogui.click(clicks=3, interval=0.01)
        pyautogui.mouseDown()
        sleep(1)
        pyautogui.mouseUp()
        pyautogui.dragTo((320, 320))

    @staticmethod
    def click():
        pyautogui.click()

    @staticmethod
    def mup():
        pyautogui.moveRel(0, -10)

    @staticmethod
    def mdown():
        pyautogui.moveRel(0, 10)

    @staticmethod
    def mright():
        pyautogui.moveRel(10, 0)

    @staticmethod
    def mleft():
        pyautogui.moveRel(-10, 0)
