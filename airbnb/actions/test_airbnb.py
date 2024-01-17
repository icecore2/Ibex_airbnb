# test_airbnb.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from search_results_page import SearchResultsPage
from highest_rating_page import HighestRatingPage

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver


def test_airbnb_workflow(driver):
    search_results_page = SearchResultsPage(driver)
    highest_rating_page = HighestRatingPage(driver)

    search_results_page.navigate_to_search_results_page()
    search_results_page.click_page_with_max_value(2)
    highest_rating_page.click_highest_rating_listing()

if __name__ == "__main__":
    pytest.main(["-v", __file__])
