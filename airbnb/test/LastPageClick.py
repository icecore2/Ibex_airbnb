import re

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver

def test_last_page_click(driver):
    driver.get("https://www.airbnb.com/s/Amsterdam--Netherlands/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Amsterdam%2C%20Netherlands&place_id=ChIJVXealLU_xkcRja_At0z9AGY&date_picker_type=calendar&checkin=2024-01-18&checkout=2024-01-19&flexible_date_search_filter_type=0&adults=2&children=1&source=structured_search_input_header&search_type=autocomplete_click")

    print("Before waiting for element with text '2'")
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='2']")))
    print("After waiting for element with text '2'")

    value = re.sub(r'\D', '', element.text)
    max_value = int(value)

    print("Before waiting for elements with numeric values")
    elements = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//a[normalize-space() and translate(text(), '0123456789', '') = '']")))

    print("After waiting for elements with numeric values")

    elements_with_numbers = []

    for e in elements:
        text = re.sub(r'\D', '', e.text)
        if text:
            elements_with_numbers.append(e)
            numeric_value = int(text)
            if numeric_value > max_value:
                max_value = numeric_value

    if max_value < 2:
        if driver.find_elements(By.XPATH, "//button[@aria-current='page']"):
            print("Only one page found")
        else:
            print("No element with numeric values found")
    else:
        for e in elements_with_numbers:
            text = re.sub(r'\D', '', e.text)
            if text == str(max_value):
                e.click()
                print("Clicked the element with the max value:", text)
                break

    if not elements_with_numbers:
        print("No element with numeric values found.")
