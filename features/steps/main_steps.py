from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(2)
    # context.driver.get("https://www.target.com/")
    # sleep(2)
    context.app.main_page.open_main()


@when("Click Sign In")
def click_sign_in(context):
    context.driver.get("https://www.target.com/account")


@when("Click Sign In from right side navigation")
def click_sign_in_from_menu(context):
    context.driver.get("https://www.target.com/login")


@then("Verify Sign In form opened")
def verify_sign_in_form(context):

    assert "login" in context.driver.current_url.lower()


@then("Verify cart is empty message is shown")
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()

