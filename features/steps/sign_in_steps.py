from behave import when, then

from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.health_popup import HealthPopup


@when('Click Account button')
def click_account_button(context):

    popup = HealthPopup(context.driver)
    popup.close_popup()

    header = Header(context.driver)
    header.click_account()


@when('Click Sign In or Create Account')
def click_sign_in_or_create_account(context):

    header = Header(context.driver)
    header.click_sign_in_create_account()


@then('Verify Sign In form opened')
def verify_sign_in_form(context):

    sign_in_page = SignInPage(context.driver)
    sign_in_page.verify_sign_in_page_opened()



