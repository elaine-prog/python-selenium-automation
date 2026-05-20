import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_INPUT = (
        By.ID,
        "search"
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-test='@web/Search/SearchButton']"
    )

    FIRST_PRODUCT = (
        By.CSS_SELECTOR,
        "a[href*='/p/']"
    )

    def search_product(self, product_name):

        search = self.find_element(self.SEARCH_INPUT)

        search.clear()

        search.send_keys(product_name)

        self.click(self.SEARCH_BUTTON)

        time.sleep(5)

    def open_first_product(self):
        first_product = self.driver.find_elements(
            *self.FIRST_PRODUCT
        )[0]

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            first_product
        )

        import time
        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            first_product
        )