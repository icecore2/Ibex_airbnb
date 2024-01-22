"""This module defines the SearchResultsPage class, which extends the BasePage class in the airbnb.infra package. The
primary purpose of this class is to provide functionality for interacting with search result pages, specifically a
method named 'click_page_with_max_value'. This method is designed to find and click on an element within the search
results based on a maximum numeric value, as specified by the 'max_value' parameter. The numeric values are extracted
from elements identified by the provided XPath constant in OrderListingConst module. The code handles scenarios such
as stale element references and sorts elements with numeric values, clicking on the one with the highest value.
Additionally, it includes informative print statements to convey the outcome of the operation."""

import re
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from airbnb.infra.BasePage import BasePage
from airbnb.infra.constans.OrderListingConst import OrderListingConst


class SearchResultsPage(BasePage):

    def click_page_with_max_value(self, max_value):
        elements = self.wait_for_elements_presence(
            By.XPATH, OrderListingConst.ELEMENT_XPATH.format(max_value)
        )

        elements_with_numbers = []
        highest_score = 0

        for e in elements:
            try:
                text = re.sub(r'\D', '', e.text)
                if text:
                    elements_with_numbers.append(e)
                    numeric_value = int(text)
                    if numeric_value > highest_score:
                        highest_score = numeric_value
            except StaleElementReferenceException:

                elements = self.wait_for_elements_presence(
                    By.XPATH, OrderListingConst.ELEMENT_XPATH.format(max_value)
                )

                elements_with_numbers = [el for el in elements_with_numbers if el in elements]
                continue

        if highest_score < 2:
            if self.driver.find_elements(By.XPATH, OrderListingConst.BUTTON_XPATH):
                print("Only one page found")
            else:
                print("No element with numeric values found.")
        else:

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
