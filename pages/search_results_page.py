from selenium.webdriver.common.by import By


SEARCH_RESULT_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

# KEEP ONLY ONE OF THESE
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/title']")

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADDED_TO_CART_TXT = (By.XPATH, "//*[text()='Added to cart']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")


# ADD THIS RIGHT HERE
class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_search_results(self, product):
        actual_result = self.driver.find_element(*SEARCH_RESULT_COUNT_TEXT).text
        assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'


