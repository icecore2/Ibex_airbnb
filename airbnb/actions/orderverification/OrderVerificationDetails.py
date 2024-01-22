import re
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrderVerificationDetails:
    def __init__(self, driver):
        self.driver = driver
        self.guests_value = 3

    def get_guests_number_locator(self):
        return By.XPATH, f"//span[contains(text(), '{self.guests_value} guest')]"

    def set_guests_value(self, guests_value):
        self.guests_value = guests_value

    def compare_date_and_guests(self):
        current_date_tomorrow = self.get_current_date_tomorrow()
        wait = WebDriverWait(self.driver, 20)

        # Get numeric value from the last CheckIn element
        numeric_value = self.get_numeric_value_from_last_element()

        check_in_locator = By.XPATH, "//div[@data-testid='change-dates-checkIn']"
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
        check_in_locator = By.XPATH, "//div[@data-testid='change-dates-checkIn']"
        elements = self.driver.find_elements(*check_in_locator)

        if elements:
            last_element = elements[-1]
            return re.sub(r'\D+', '', last_element.text)
        else:
            print("No element with value '' found.")
            return None
