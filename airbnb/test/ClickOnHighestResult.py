import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver


def test_highest_rating_listing(driver):
<<<<<<< HEAD
    # Open the provided Airbnb URL
    driver.get(
        "https://www.airbnb.com/s/Amsterdam--Netherlands/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Amsterdam%2C%20Netherlands&place_id=ChIJVXealLU_xkcRja_At0z9AGY&date_picker_type=calendar&checkin=2024-01-18&checkout=2024-01-19&flexible_date_search_filter_type=0&adults=2&children=1&source=structured_search_input_header&search_type=autocomplete_click&price_filter_num_nights=1&federated_search_session_id=747cbb7b-be91-49c2-976d-5691d532702f&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoyNTIsInZlcnNpb24iOjF9")

    # Wait for elements to be present
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@aria-label]')))

    # Locate all elements with the specified XPath pattern
    rating_elements = driver.find_elements(By.XPATH, '//span[@aria-label]')

    # Initialize an empty list to store tuples of (rating, reviews, element)
    ratings_list = []

    # Loop through each element, extract the numeric part from aria-label and add to the list
=======

    driver.get(
        "https://www.airbnb.com/s/Amsterdam--Netherlands/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Amsterdam%2C%20Netherlands&place_id=ChIJVXealLU_xkcRja_At0z9AGY&date_picker_type=calendar&checkin=2024-01-18&checkout=2024-01-19&flexible_date_search_filter_type=0&adults=2&children=1&source=structured_search_input_header&search_type=autocomplete_click&price_filter_num_nights=1&federated_search_session_id=747cbb7b-be91-49c2-976d-5691d532702f&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoyNTIsInZlcnNpb24iOjF9")


    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@aria-label]')))


    rating_elements = driver.find_elements(By.XPATH, '//span[@aria-label]')


    ratings_list = []


>>>>>>> 3b80405 (ClickOnHighest result .)
    for element in rating_elements:
        aria_label = element.get_attribute('aria-label')
        print("Aria Label:", aria_label)

<<<<<<< HEAD
        # Use try-except block to handle elements without numeric ratings
        try:
            # Extract the numeric part from aria-label using a regular expression
            rating = float(''.join(c for c in aria_label if c.isdigit() or c == '.'))
            reviews = int(''.join(c for c in aria_label if c.isdigit()))

            # Append tuple (rating, reviews, element) to the list
            ratings_list.append((rating, reviews, element))
        except ValueError:
            # Skip this element if it cannot be converted to a float
            print("Skipping element:", aria_label)

    if not ratings_list:
        # If ratings_list is empty, print a message and exit the test
        print("No elements found with the specified XPath pattern")
        return

    # Sort the ratings_list based on rating (descending) and reviews (descending)
    sorted_ratings = sorted(ratings_list, key=lambda x: (x[0], x[1]), reverse=True)

    # Find the element with the highest rating and maximum reviews
    highest_rating_element = sorted_ratings[0][2]

    # Ensure the element is clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@aria-label]')))

    # Use ActionChains for a more reliable click
    ActionChains(driver).move_to_element(highest_rating_element).click().perform()

    # Add any additional assertions or actions based on your requirements
=======

        try:

            rating = float(''.join(c for c in aria_label if c.isdigit() or c == '.'))
            reviews = int(''.join(c for c in aria_label if c.isdigit()))


            ratings_list.append((rating, reviews, element))
        except ValueError:

            print("Skipping element:", aria_label)

    if not ratings_list:

        print("No elements found with the specified XPath pattern")
        return


    sorted_ratings = sorted(ratings_list, key=lambda x: (x[0], x[1]), reverse=True)


    highest_rating_element = sorted_ratings[0][2]


    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[@aria-label]')))


    ActionChains(driver).move_to_element(highest_rating_element).click().perform()


>>>>>>> 3b80405 (ClickOnHighest result .)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
