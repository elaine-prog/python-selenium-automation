from behave import given, when, then

from pages.sign_in_terms_page import SignInTermsPage


@given('Open sign in page')
def open_sign_in_page(context):
    context.driver.get(
        "https://www.target.com/orders?lnk=acct_nav_my_account"
    )


@when('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Target terms and conditions link')
def click_terms_link(context):
    sign_in_page = SignInTermsPage(context.driver)
    sign_in_page.click_terms_link()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    all_windows = context.driver.window_handles

    for window in all_windows:
        if window != context.original_window:
            context.driver.switch_to.window(window)
            break


@then('Verify Terms and Conditions page is opened')
def verify_terms_page_opened(context):
    assert "terms" in context.driver.current_url.lower()


@then('User can close new window and switch back to original')
def close_new_window_and_return(context):
    context.driver.close()

    context.driver.switch_to.window(
        context.original_window
    )

    assert "target.com" in context.driver.current_url