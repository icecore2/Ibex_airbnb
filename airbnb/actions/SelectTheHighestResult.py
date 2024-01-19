import re

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from airbnb.infra.BasePage import BasePage


class SelectTheHighestResult(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_page_with_max_value(self, max_value):
        elements = self.wait_for_elements_presence(
            By.XPATH, "//a[normalize-space() and translate(text(), '0123456789', '') = '']"
        )

        elements_with_numbers = []
        highest_score = 0  # Track the highest score

        for e in elements:
            try:
                text = re.sub(r'\D', '', e.text)
                if text:
                    elements_with_numbers.append(e)
                    numeric_value = int(text)
                    if numeric_value > max_value:
                        max_value = numeric_value
                    if numeric_value > highest_score:
                        highest_score = numeric_value
            except StaleElementReferenceException:
                # Handle StaleElementReferenceException by attempting to locate the element again
                elements = self.wait_for_elements_presence(
                    By.XPATH, "//a[normalize-space() and translate(text(), '0123456789', '') = '']"
                )
                continue

        if highest_score < 2:
            if self.driver.find_elements(By.XPATH, "//button[@aria-current='page']"):
                print("Only one page found")
            else:
                print("No element with numeric values found.")
        else:
            # Sort the elements_with_numbers list in descending order based on the numeric value
            elements_with_numbers.sort(key=lambda e: int(re.sub(r'\D', '', e.text)), reverse=True)
            for e in elements_with_numbers:
                text = re.sub(r'\D', '', e.text)
                if text == str(highest_score):
                    e.click()
                    print("Clicked the element with the max value:", text)
                    break

            if not elements_with_numbers:
                print("No element with numeric values found.")

        print(f"Highest Score: {highest_score}")  # Print the highest score


    def get_ratings_list(self):
        rating_elements = self.wait_for_elements_presence(By.XPATH, '//span[@aria-label]')

        ratings_list = []

        for element in rating_elements:
            aria_label = element.get_attribute('aria-label')
            print("Aria Label:", aria_label)

            try:
                rating = float(''.join(c for c in aria_label if c.isdigit() or c == '.'))
                reviews = int(''.join(c for c in aria_label if c.isdigit()))

                ratings_list.append((rating, reviews, element))
            except ValueError:
                print("Skipping element:", aria_label)

        return ratings_list

    def click_highest_rating_listing(self):
        ratings_list = self.get_ratings_list()

        if not ratings_list:
            print("No elements found with the specified XPath pattern")
            return

        sorted_ratings = sorted(ratings_list, key=lambda x: (x[0], x[1]), reverse=True)
        highest_rating_element = sorted_ratings[0][2]

        self.wait_for_element_presence(
            By.XPATH, '//span[@aria-label]'
        )

        ActionChains(self.driver).move_to_element(highest_rating_element).click().perform()
