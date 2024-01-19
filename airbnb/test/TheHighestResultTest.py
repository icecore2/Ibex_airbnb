import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from airbnb.actions.SelectTheHighestResult import SelectTheHighestResult

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver


def test_select_the_highest_result(driver):
    # Set the initial URL
    initial_url = "https://www.airbnb.com/s/Amsterdam--Netherlands/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Amsterdam%2C%20Netherlands&place_id=ChIJVXealLU_xkcRja_At0z9AGY&date_picker_type=calendar&checkin=2024-01-20&checkout=2024-01-21&flexible_date_search_filter_type=0&adults=2&children=1&source=structured_search_input_header&search_type=autocomplete_click"

    # Navigate to the initial URL
    driver.get(initial_url)

    select_highest_result = SelectTheHighestResult(driver)

    # Perform actions using the SelectTheHighestResult class
    select_highest_result.click_page_with_max_value(0)

if __name__ == "__main__":
    pytest.main(["-v", __file__])
