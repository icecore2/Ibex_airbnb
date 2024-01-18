import re

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from airbnb.infra.BasePage import BasePage


class SearchResultsPage(BasePage):

    URL = "https://www.airbnb.com/s/Amsterdam--Netherlands/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Amsterdam%2C%20Netherlands&place_id=ChIJVXealLU_xkcRja_At0z9AGY&date_picker_type=calendar&checkin=2024-01-18&checkout=2024-01-19&flexible_date_search_filter_type=0&adults=2&children=1&source=structured_search_input_header&search_type=autocomplete_click"

    def navigate_to_search_results_page(self):
        self.driver.get(self.URL)

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
