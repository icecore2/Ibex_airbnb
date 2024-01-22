

import re

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from airbnb.infra.BasePage import BasePage


class SearchResultsPage(BasePage):

    def click_page_with_max_value(self, max_value):
        elements = self.wait_for_elements_presence(
            By.XPATH, "//a[normalize-space()='{}']".format(max_value)

        )

        elements_with_numbers = []
        highest_score = 0  # Track the highest score

        for e in elements:
            try:
                text = re.sub(r'\D', '', e.text)
                if text:
                    elements_with_numbers.append(e)
                    numeric_value = int(text)
                    if numeric_value > highest_score:
                        highest_score = numeric_value
            except StaleElementReferenceException:
                # Handle StaleElementReferenceException by attempting to locate the element again
                elements = self.wait_for_elements_presence(
                    By.XPATH, "//a[normalize-space()='{}']".format(max_value)
                )
                # Remove stale elements from the list
                elements_with_numbers = [el for el in elements_with_numbers if el in elements]
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

