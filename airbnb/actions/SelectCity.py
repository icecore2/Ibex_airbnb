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

        # Wait for the element to be clickable
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='bigsearch-query-location-input']"))
            )
        except:
            print("Element not found after 10 seconds")

        # Proceed with element interaction if found
        element.click()
        text = element.get_attribute("value")
        print("The text is:", text)

if __name__ == "__main__":
    unittest.main()
