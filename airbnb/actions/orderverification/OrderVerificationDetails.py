"""This module defines the OrderVerificationDetails class, which facilitates the verification of order details on the
Airbnb platform. The class utilizes Selenium WebDriver for browser automation and interacts with various elements on
the web page, such as CheckIn dates and numeric values. The primary purpose of this class is to compare the CheckIn
date and numeric value of the last CheckIn element against expected values. The code includes methods like
'compare_date_and_guests', 'get_current_date_tomorrow', and 'get_numeric_value_from_last_element'. The XPaths for
different page elements are defined in the OrderVerificationConst module. Additionally, the class allows setting the
expected guests value dynamically. The verification process checks if the CheckIn date matches tomorrow's date and
the numeric value matches the expected guests value, providing informative print statements in case of discrepancies."""

import re
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from airbnb.infra.constans.OrderVerificationConst import OrderVerificationConst


class OrderVerificationDetails:
    def __init__(self, driver):
        self.driver = driver
        self.guests_value = 3

    def get_guests_number_locator(self):
        return By.XPATH, OrderVerificationConst.GUESTS_NUMBER_XPATH.format(self.guests_value)

    def set_guests_value(self, guests_value):
        self.guests_value = guests_value

    def compare_date_and_guests(self):
        current_date_tomorrow = self.get_current_date_tomorrow()
        wait = WebDriverWait(self.driver, 20)

        # Get numeric value from the last CheckIn element
        numeric_value = self.get_numeric_value_from_last_element()

        check_in_locator = By.XPATH, OrderVerificationConst.CHECK_IN_XPATH
        check_in_elements = wait.until(EC.presence_of_all_elements_located(check_in_locator))

        if check_in_elements:
            check_in_element = check_in_elements[-1]
            wait.until(EC.visibility_of(check_in_element))
            check_in_date = check_in_element.text
            print("CheckIn Date:", check_in_date)

            # Check if CheckIn Date matches tomorrow's date and numeric value matches
            if check_in_date != current_date_tomorrow or numeric_value != str(self.guests_value):
                print("CheckIn Date or Numeric Value does not match.")
                return False
        else:
            print("No CheckIn element found.")
            return False

        return True

    def get_current_date_tomorrow(self):
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.strftime("%m/%d/%Y")

    def get_numeric_value_from_last_element(self):
        check_in_locator = By.XPATH, OrderVerificationConst.CHECK_IN_XPATH
        elements = self.driver.find_elements(*check_in_locator)

        if elements:
            last_element = elements[-1]
            return re.sub(r'\D+', '', last_element.text)
        else:
            print("No element with value '' found.")
            return None
