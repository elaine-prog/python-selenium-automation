from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignInTermsPage(BasePage):

    TERMS_LINK = (
        By.CSS_SELECTOR,
        "a[href*='terms-conditions']"
    )

    def click_terms_link(self):
        self.click(self.TERMS_LINK)