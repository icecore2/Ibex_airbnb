import time
import pyautogui


class CloseAlert:
    def __init__(self, driver):
        self.driver = driver

    def perform_robot_actions(self):
        try:
            # Add a delay of 3 seconds
            time.sleep(3)

            # Press the TAB key
            pyautogui.press('tab')

            # Press the ENTER key
            pyautogui.press('enter')

        except Exception as e:
            print(e)
