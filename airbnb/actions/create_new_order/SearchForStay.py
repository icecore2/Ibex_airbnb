"""This module defines the SearchForStay class, which encapsulates the functionality for performing a search for a
stay on the Airbnb platform. The class utilizes Selenium WebDriver for browser automation and interacts with various
elements on the web page, such as search input, date selection, guest count, and the search button. The code includes
methods like 'city_search', 'select_dates', 'select_guests', 'verify_guests_count', and 'click_search_button' to
navigate through the search process, and it handles potential timeouts with informative print statements. The XPaths
for different page elements are defined in the OrderSearchConst module. Overall, the class facilitates the automation
of the Airbnb search process with configurable inputs such as location, dates, and guest counts."""

from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from airbnb.infra.constans.OrderSearchConst import OrderSearchConst


class SearchForStay:

    def __init__(self, driver):
        self.driver = driver
        self.url = OrderSearchConst.URL
        self.search_input_xpath = OrderSearchConst.SEARCH_INPUT_XPATH
        self.dropdown_option_xpath = OrderSearchConst.DROPDOWN_OPTION_XPATH
        self.date_xpath_format = OrderSearchConst.DATE_XPATH  # Change the attribute name
        self.one_day_plus_xpath = OrderSearchConst.ONE_DAY_PLUS_XPATH
        self.guests_button_xpath = OrderSearchConst.GUESTS_BUTTON_XPATH
        self.adults_increase_button_xpath = OrderSearchConst.ADULTS_INCREASE_BUTTON_XPATH
        self.children_increase_button_xpath = OrderSearchConst.CHILDREN_INCREASE_BUTTON_XPATH
        self.adults_count_xpath = OrderSearchConst.ADULTS_COUNT_XPATH
        self.children_count_xpath = OrderSearchConst.CHILDREN_COUNT_XPATH
        self.search_button_xpath = OrderSearchConst.SEARCH_BUTTON_XPATH

    def navigate_to_airbnb(self):
        self.driver.get(self.url)

    def city_search(self, location):
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.search_input_xpath))
            )
        except:
            print("Search input element not found after 10 seconds")

        search_input.send_keys(location)

        try:
            dropdown_option = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.dropdown_option_xpath))
            )
        except:
            print(f"Dropdown option for {location} not found after sending keys")

        dropdown_option.click()

    def select_dates(self):
        current_date = datetime.now()
        next_day = current_date + timedelta(days=1)

        current_date_str = current_date.strftime("%m/%d/%Y")
        next_day_str = next_day.strftime("%m/%d/%Y")

        checkin_date_xpath = self.date_xpath_format.format(next_day_str)
        checkout_date_xpath = self.date_xpath_format.format(next_day_str)

        try:
            checkin_date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, checkin_date_xpath))
            )
        except:
            print("Check-in date element not found after 10 seconds")

        checkin_date.click()

        try:
            checkout_date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, checkout_date_xpath))
            )
        except:
            print("Check-out date element not found after selecting check-in date")

        checkout_date.click()

        try:
            one_day_plus = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.one_day_plus_xpath))
            )
        except:
            print("One day plus element not found after selecting check-out date")

        one_day_plus.click()

    def select_guests(self):
        try:
            guests_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.guests_button_xpath))
            )
        except:
            print("Guests button element not found after 10 seconds")

        guests_button.click()

        try:
            adults_increase_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.adults_increase_button_xpath))
            )
        except:
            print("Adults increase button not found after clicking on guests button")

        adults_increase_button.click()
        adults_increase_button.click()  # Additional click

        try:
            children_increase_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.children_increase_button_xpath))
            )
        except:
            print("Children increase button not found after clicking on guests button")

        children_increase_button.click()

    def verify_guests_count(self):
        try:
            adults_count = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.adults_count_xpath))
            )
        except:
            print("Adults count element not found after selecting guests")

        try:
            children_count = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.children_count_xpath))
            )
        except:
            print("Children count element not found after selecting guests")

        assert adults_count.text == "2 Adults", "Number of adults is incorrect"
        assert children_count.text == "1 Children", "Number of children is incorrect"

    def click_search_button(self):
        try:
            search_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))
            )
        except:
            print("Search button not found after selecting guests")
            return

        try:
            search_button.click()
        except:
            self.driver.execute_script("arguments[0].click();", search_button)
