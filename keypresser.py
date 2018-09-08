import pyautogui
from time import sleep

class Keypresser:
    def one_mouse_click(self, x):
        pyautogui.moveTo(x)
        pyautogui.click()

    def two_mouse_click(self, x):
        pyautogui.moveTo(x)
        pyautogui.click()
        sleep(0.1)
        pyautogui.click()
        
    def triple_click_300(self):
        pyautogui.moveTo((300,300))
        pyautogui.click(clicks=3, interval=0.01)
        pyautogui.mouseDown()
        sleep(1)
        pyautogui.mouseUp()
        pyautogui.dragTo((320,320))

    def click(self):
        pyautogui.click()

    def mup(self):
        pyautogui.moveRel(0,-10)

    def mdown(self):
        pyautogui.moveRel(0,10)

    def mright(self):
        pyautogui.moveRel(10,0)

    def mleft(self):
        pyautogui.moveRel(-10,0)
