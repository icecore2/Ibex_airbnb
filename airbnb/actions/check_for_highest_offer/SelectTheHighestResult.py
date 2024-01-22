
"""This module defines the SelectTheHighestResult class, which extends the BasePage class in the airbnb. Infra
package. The primary purpose of this class is to provide functionality for interacting with search results and
selecting the listing with the highest numeric rating. The class includes methods such as 'click_page_with_max_value'
to click on an element within the search results based on a maximum numeric value and 'click_highest_rating_listing'
to click on the listing with the highest rating. The code also extracts ratings information from elements identified
by the provided XPaths in the OrderListingConst module, handles scenarios such as stale element references,
and includes informative print statements to convey the outcome of the operations."""

import re
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from airbnb.infra.BasePage import BasePage
from airbnb.infra.constans.OrderListingConst import OrderListingConst


class SelectTheHighestResult(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_page_with_max_value(self, max_value):
        elements = self.wait_for_elements_presence(
            By.XPATH, OrderListingConst.ELEMENT_XPATH
        )

        elements_with_numbers = []
        highest_score = 0

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

                elements = self.wait_for_elements_presence(
                    By.XPATH, OrderListingConst.ELEMENT_XPATH
                )
                continue

        if highest_score < 2:
            if self.driver.find_elements(By.XPATH, OrderListingConst.BUTTON_XPATH):
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

        print(f"Highest Score: {highest_score}")

    def get_ratings_list(self):
        rating_elements = self.wait_for_elements_presence(By.XPATH, OrderListingConst.RATING_XPATH)

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
            By.XPATH, OrderListingConst.RATING_XPATH
        )

        ActionChains(self.driver).move_to_element(highest_rating_element).click().perform()
