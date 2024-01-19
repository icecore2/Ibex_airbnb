import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchForStay:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.airbnb.com/"
        self.search_input_xpath = "//input[@id='bigsearch-query-location-input']"
        self.dropdown_option_xpath = "//div[contains(text(), 'Amsterdam, Netherlands')]"
        self.checkin_date_xpath = "//div[@data-testid='calendar-day-01/20/2024']"
        self.checkout_date_xpath = "//div[@data-testid='calendar-day-01/20/2024']"
        self.one_day_plus_xpath = "//span[normalize-space()='1 day']"
        self.guests_button_xpath = "//div[text()='Who']/following-sibling::div[text()='Add guests']"
        self.adults_increase_button_xpath = "//button[@data-testid='stepper-adults-increase-button']"
        self.children_increase_button_xpath = "//button[@data-testid='stepper-children-increase-button']"
        self.adults_count_xpath = "//span[normalize-space()='2 Adults']"
        self.children_count_xpath = "//span[normalize-space()='1 Children']"
        self.search_button_xpath = "//div[ '*'and text()='Search']"

    def navigate_to_airbnb(self):
        self.driver.get(self.url)

    def city_search(self, location):
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.search_input_xpath))
            )
        except:
            print("Search input element not found after 10 seconds")

        # Send keys to the search input field
        search_input.send_keys(location)

        try:
            dropdown_option = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.dropdown_option_xpath))
            )
        except:
            print(f"Dropdown option for {location} not found after sending keys")

        # Click on the dropdown option
        dropdown_option.click()

    def select_dates(self):
        try:
            checkin_date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.checkin_date_xpath))
            )
        except:
            print("Check-in date element not found after 10 seconds")

        # Click on the check-in date
        checkin_date.click()

        try:
            checkout_date = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.checkout_date_xpath))
            )
        except:
            print("Check-out date element not found after selecting check-in date")

        # Click on the checkout date
        checkout_date.click()

        try:
            one_day_plus = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.one_day_plus_xpath))
            )
        except:
            print("One day plus element not found after selecting check-out date")

        # Click on "1 day plus"
        one_day_plus.click()

    def select_guests(self):
        try:
            guests_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.guests_button_xpath))
            )
        except:
            print("Guests button element not found after 10 seconds")

        # Click on the guests button
        guests_button.click()

        try:
            adults_increase_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.adults_increase_button_xpath))
            )
        except:
            print("Adults increase button not found after clicking on guests button")

        # Click on the increase button for adults
        adults_increase_button.click()
        adults_increase_button.click()  # Additional click

        try:
            children_increase_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.children_increase_button_xpath))
            )
        except:
            print("Children increase button not found after clicking on guests button")

        # Click on the increase button for children
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
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.search_button_xpath))
            )
        except:
            print("Search button not found after selecting guests")
