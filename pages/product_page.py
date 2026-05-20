from selenium.webdriver.common.by import By
import time

from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-test='orderPickupButton']"
    )

    def add_to_cart(self):

        button = self.find_element(
            self.ADD_TO_CART_BUTTON
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            button
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

