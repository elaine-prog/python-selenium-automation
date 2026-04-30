from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")



@when("Click on cart icon")
def click_cart_icon(context):
    context.driver.get("https://www.target.com/cart")



@then("Verify cart is empty message is shown")
def verify_empty_cart(context):
    print("CURRENT URL:", context.driver.current_url)
    time.sleep(10)
    assert "/cart" in context.driver.current_url


@when("Click Sign In")
def click_sign_in(context):
    context.driver.get("https://www.target.com/account")


@when("Click Sign In from right side navigation")
def click_sign_in_from_menu(context):
    context.driver.get("https://www.target.com/login")


@then("Verify Sign In form opened")
def verify_sign_in_form(context):
    print("CURRENT URL:", context.driver.current_url)
    time.sleep(5)

    assert "login" in context.driver.current_url