# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from airbnb.infra.BasePage import BasePage
#
#
# class HighestRatingPage(BasePage):
#     def get_ratings_list(self):
#         rating_elements = self.wait_for_elements_presence(By.XPATH, '//span[@aria-label]')
#
#         ratings_list = []
#
#         for element in rating_elements:
#             aria_label = element.get_attribute('aria-label')
#             print("Aria Label:", aria_label)
#
#             try:
#                 rating = float(''.join(c for c in aria_label if c.isdigit() or c == '.'))
#                 reviews = int(''.join(c for c in aria_label if c.isdigit()))
#
#                 ratings_list.append((rating, reviews, element))
#             except ValueError:
#                 print("Skipping element:", aria_label)
#
#         return ratings_list
#
#     def click_highest_rating_listing(self):
#         ratings_list = self.get_ratings_list()
#
#         if not ratings_list:
#             print("No elements found with the specified XPath pattern")
#             return
#
#         sorted_ratings = sorted(ratings_list, key=lambda x: (x[0], x[1]), reverse=True)
#         highest_rating_element = sorted_ratings[0][2]
#
#         self.wait_for_element_presence(
#             By.XPATH, '//span[@aria-label]'
#         )
#
#         ActionChains(self.driver).move_to_element(highest_rating_element).click().perform()
