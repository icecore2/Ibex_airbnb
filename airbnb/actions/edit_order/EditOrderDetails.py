"""This module defines the EditOrderDetails class, which is responsible for automating the process of editing order
details on the Airbnb platform. The class utilizes Selenium WebDriver for browser automation and interacts with
various elements on the web page, such as guests dropdown, date pickers, and date inputs. The code includes methods
like 'edit_guests_number', 'change_dates', and 'set_date_picker_value' to modify the number of guests and change
reservation dates. The XPaths for different page elements are defined in the EditConst module. The class provides
functionality to open dropdowns, click buttons, and input new date values, and it verifies the changes made to guests
count and reservation dates. Additionally, the code incorporates WebDriverWait for handling potential delays during
element interactions."""


from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from airbnb.infra.constans.EditConst import EditConst


class EditOrderDetails:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def edit_guests_number(self):
        guests_dropdown_locator = By.XPATH, EditConst.GUESTS_DROPDOWN_XPATH
        decrease_button_locator = By.XPATH, EditConst.DECREASE_BUTTON_XPATH

        # Open the Guests dropdown
        guests_dropdown = self.wait.until(EC.element_to_be_clickable(guests_dropdown_locator))
        guests_dropdown.click()

        # Click on the decrease button
        decrease_button = self.wait.until(EC.element_to_be_clickable(decrease_button_locator))
        decrease_button.click()

        # Verify the number of children is now '0'
        children_count_locator = By.XPATH, EditConst.CHILDREN_COUNT_XPATH
        children_count = self.wait.until(EC.visibility_of_element_located(children_count_locator))
        children_count_text = children_count.text.strip()
        assert children_count_text == "0", "Children count is not '0'."

    def change_dates(self):
        check_in_locator = By.XPATH, EditConst.CHECK_IN_XPATH
        check_out_locator = By.XPATH, EditConst.CHECK_OUT_XPATH

        # Click on CheckIn and CheckOut to open date pickers
        check_in_element = self.wait.until(EC.element_to_be_clickable(check_in_locator))
        check_in_element.click()

        check_out_element = self.wait.until(EC.element_to_be_clickable(check_out_locator))
        check_out_element.click()

        # Calculate new dates (a week from tomorrow)
        tomorrow = datetime.now() + timedelta(days=1)
        new_check_in_date = tomorrow + timedelta(days=7)
        new_check_out_date = new_check_in_date + timedelta(days=7)

        formatter = "%m/%d/%Y"
        formatted_check_in = new_check_in_date.strftime(formatter)
        formatted_check_out = new_check_out_date.strftime(formatter)

        self.set_date_picker_value(check_in_locator, formatted_check_in)
        self.set_date_picker_value(check_out_locator, formatted_check_out)

        updated_check_in_element = self.driver.find_element(*check_in_locator)
        updated_check_out_element = self.driver.find_element(*check_out_locator)
        assert updated_check_in_element.text == formatted_check_in, "CheckIn date not updated."
        assert updated_check_out_element.text == formatted_check_out, "CheckOut date not updated."

    def set_date_picker_value(self, datepicker_locator, value):
        date_input_locator = By.XPATH, f"{datepicker_locator[1]}//input[@type='text']"
        date_input = self.wait.until(EC.element_to_be_clickable(date_input_locator))
        date_input.clear()
        date_input.send_keys(value)
