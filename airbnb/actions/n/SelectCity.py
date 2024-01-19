import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class SelectCity(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def test_search_location(self):
        self.driver.get("https://www.airbnb.com/")

        # Wait for the search input field to be clickable
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='bigsearch-query-location-input']"))
            )
        except:
            print("Search input element not found after 10 seconds")

        # Send keys to the search input field
        search_input.send_keys("Amsterdam, Netherlands")

        # Wait for the dropdown list to appear
        try:
            dropdown_option = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div['*' and text()='Amsterdam, Netherlands']"))
            )
        except:
            print("Dropdown option not found after sending keys")

        # Click on the first option in the dropdown list
        dropdown_option.click()

if __name__ == "__main__":
    unittest.main()


