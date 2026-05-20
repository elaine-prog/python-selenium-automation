from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignInPage(BasePage):

    SIGN_IN_HEADER = (
        By.CSS_SELECTOR,
        "h1"
    )

    def verify_sign_in_page_opened(self):

        assert "login" in self.driver.current_url

        header = self.find_element(self.SIGN_IN_HEADER)

        assert "Sign in" in header.text