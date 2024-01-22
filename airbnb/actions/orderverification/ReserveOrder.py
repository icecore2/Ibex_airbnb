
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReserveOrder:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_reserve_button_and_verify_request_to_book_page(self):
        reserve_button_locator = By.XPATH, "//span[normalize-space()='Reserve']"

        # Click on the 'Reserve' button using JavaScript
        reserve_button = self.wait.until(EC.element_to_be_clickable(reserve_button_locator))
        self.driver.execute_script("arguments[0].click();", reserve_button)

        request_to_book_page_locator = By.XPATH, "//h1[contains(text(), 'Request to book')]"
        request_to_book_page = self.wait.until(EC.visibility_of_element_located(request_to_book_page_locator))
        assert request_to_book_page.is_displayed(), ("Request to book page did not appear after clicking the Reserve "
                                                     "button.")
