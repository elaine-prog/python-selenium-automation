from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HealthPopup:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def close_popup(self):

        try:
            continue_button = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(., 'Continue shopping')]"
                    )
                )
            )

            continue_button.click()

            print("Popup closed")

        except TimeoutException:
            print("Popup not shown")