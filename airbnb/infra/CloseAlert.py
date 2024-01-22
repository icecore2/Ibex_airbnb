import time
import pyautogui


class CloseAlert:
    def __init__(self, driver):
        self.driver = driver

    def perform_robot_actions(self):
        try:
            # Add a delay of 3 seconds
            time.sleep(3)


            pyautogui.press('tab')


            pyautogui.press('enter')

        except Exception as e:
            print(e)
