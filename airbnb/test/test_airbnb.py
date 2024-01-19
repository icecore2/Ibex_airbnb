# # test_airbnb.py
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from airbnb.actions.search_results_page import SearchResultsPage
# from airbnb.actions.highest_rating_page import HighestRatingPage
#
# @pytest.fixture(scope="module")
# def driver():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     yield driver
#
#
# def test_airbnb_workflow(driver):
#     search_results_page = SearchResultsPage(driver)
#     highest_rating_page = HighestRatingPage(driver)
#
#     search_results_page.navigate_to_search_results_page()
#     search_results_page.click_page_with_max_value(2)
#     highest_rating_page.click_highest_rating_listing()
#
# if __name__ == "__main__":
#     pytest.main(["-v", __file__])
#
#
#
#
#

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# from airbnb.actions.SearchForStay import SearchForStay
#
#
# @pytest.fixture(scope="module")
# def driver():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# def test_airbnb_workflow(driver):
#     search_for_stay = SearchForStay(driver)
#
#
#     search_for_stay.navigate_to_airbnb()
#     search_for_stay.city_search("Amsterdam, Netherlands")
#     search_for_stay.select_dates()
#     search_for_stay.select_guests()
#     search_for_stay.verify_guests_count()
#
#
# if __name__ == "__main__":
#     pytest.main(["-v", __file__])
#


# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from airbnb.actions.SearchForStay import SearchForStay
# from airbnb.actions.SelectTheHighestResult import SelectTheHighestResult
#
# @pytest.fixture(scope="module")
# def driver():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     yield driver
#
#
# def test_search_for_stay(driver):
#     search_for_stay = SearchForStay(driver)
#
#
#
#     search_for_stay.navigate_to_airbnb()
#     search_for_stay.city_search("Amsterdam, Netherlands")
#     search_for_stay.select_dates()
#     search_for_stay.select_guests()
#     search_for_stay.verify_guests_count()
#
# def test_select_highest_result(driver):
#     select_highest_result = SelectTheHighestResult(driver)
#
#     # Wait for the element with text 'Your search' to appear
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Your search')]"))
#     )
#
#     # Continue with the rest of your test steps
#     select_highest_result.click_page_with_max_value(0)
#
# if __name__ == "__main__":
#     pytest.main(["-v", __file__])
#
#


#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from airbnb.actions.search_results_page import SearchResultsPage
# from airbnb.actions.highest_rating_page import HighestRatingPage
#
# @pytest.fixture(scope="module")
# def driver():
#     chrome_options = Options()
#     chrome_options.add_experimental_option("detach", True)
#
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     yield driver
#
#
# def test_airbnb_workflow(driver):
#     search_results_page = SearchResultsPage(driver)
#     highest_rating_page = HighestRatingPage(driver)
#
#     search_results_page.navigate_to_search_results_page()
#     search_results_page.click_page_with_max_value(2)
#     highest_rating_page.click_highest_rating_listing()
#
# if __name__ == "__main__":
#     pytest.main(["-v", __file__])








import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from  airbnb.actions.SearchForStay import SearchForStay
from airbnb.actions.search_results_page import SearchResultsPage
from airbnb.actions.SelectTheHighestResult import SelectTheHighestResult




@pytest.fixture(scope="module")
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.airbnb.com/")
    driver.maximize_window()
    yield driver


@pytest.mark.priority1
def test_search_staying(setup):
    search_for_stay = SearchForStay(setup)
    search_for_stay.city_search("Amsterdam, Netherlands")
    search_for_stay.select_dates()
    search_for_stay.select_guests()
    search_for_stay.verify_guests_count()
    search_for_stay.click_search_button()

@pytest.mark.priority2
def test_airbnb_workflow(setup):
    search_results_page = SearchResultsPage(setup)
    select_the_highest_result = SelectTheHighestResult(setup)

    search_results_page.click_page_with_max_value(2)
    select_the_highest_result.click_highest_rating_listing()



if __name__ == "__main__":
    pytest.main(["-v", __file__])
