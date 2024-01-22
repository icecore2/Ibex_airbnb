import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from airbnb.actions.edit_order.EditOrderDetails import EditOrderDetails
from airbnb.actions.orderverification.OrderVerificationDetails import OrderVerificationDetails
from airbnb.actions.orderverification.ReserveOrder import ReserveOrder
from airbnb.actions.create_new_order.SearchForStay import SearchForStay
from airbnb.actions.check_for_highest_offer.SelectTheHighestResult import SelectTheHighestResult
from airbnb.actions.check_for_highest_offer.search_results_page import SearchResultsPage
from airbnb.infra.CloseAlert import CloseAlert


@pytest.fixture(scope="module")
def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.airbnb.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


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
    search_results_page.click_page_with_max_value(15)
    select_the_highest_result.click_highest_rating_listing()


@pytest.mark.priority3
def test_close_alert(setup):
    close_alert = CloseAlert(setup)
    close_alert.perform_robot_actions()


@pytest.mark.priority4
def test_search_for_text(setup):
    order_verification_details = OrderVerificationDetails(setup)
    order_verification_details.set_guests_value(3)
    order_verification_details.compare_date_and_guests()


@pytest.mark.priority5
def test_edit_order(setup):
    edit_order_details = EditOrderDetails(setup)
    edit_order_details.edit_guests_number()
    edit_order_details.change_dates()


@pytest.mark.priority6
def test_reserve(setup):
    reserve_order = ReserveOrder(setup)
    reserve_order.click_reserve_button_and_verify_request_to_book_page()


if __name__ == "__main__":
    pytest.main(["-v", __file__])
