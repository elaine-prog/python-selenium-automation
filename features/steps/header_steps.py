from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


@when('Click on Cart icon')
def click_cart(context):
    context.app.cart_page.open_cart()

@when("Search for {search_query}")
def search_product(context, search_query):
    context.app.header.search_product(search_query)


@then("Verify header link container is shown")
def verify_header_links(context):
    e = context.driver.find_element(By.CSS_SELECTOR, "[class*='HeaderLinksContainer']")
    print('\nHeader links container: ')
    print(e)


@then("Verify {expected_amount} links are shown")
def verify_header_link_amount(context, expected_amount):  #  expected_amount = "6"
    expected_amount = int(expected_amount) # expected_amount "6" => 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='HeaderLinksContainer'] a")
    print('\nHeader links: ')
    print(links)
    # assert 6 == 6
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'