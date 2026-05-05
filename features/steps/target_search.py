from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    wait = WebDriverWait(context.driver, 10)

    empty_text = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'empty')]")
        )
    )

    assert empty_text is not None


@when("Click Sign In")
def click_sign_in(context):
    context.driver.get("https://www.target.com/account")


@when("Click Sign In from right side navigation")
def click_sign_in_from_menu(context):
    context.driver.get("https://www.target.com/login")


@then("Verify Sign In form opened")
def verify_sign_in_form(context):
    wait = WebDriverWait(context.driver, 10)

    email_field = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    assert email_field is not None


@when('Search for "{item}"')
def search_product(context, item):
    wait = WebDriverWait(context.driver, 10)

    search_box = wait.until(
        EC.element_to_be_clickable((By.NAME, "searchTerm"))
    )

    search_box.clear()
    search_box.send_keys(item)
    search_box.send_keys(Keys.ENTER)


@then('Verify search results for "{item}" shown')
def verify_search_results(context, item):
    wait = WebDriverWait(context.driver, 10)

    # wait for page to load
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # find_elements → multiple elements
    results = context.driver.find_elements(
        By.XPATH, "//a[contains(@href,'/p/')]"
    )

    assert len(results) > 0, f"No results found for {item}"


@given("Open Target Circle page")
def open_target_circle(context):
    context.driver.get("https://www.target.com/circle")


@then("Verify there are 2 story cards under Unlock added value")
def verify_story_cards(context):
    wait = WebDriverWait(context.driver, 10)

    header = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Unlock added value')]")
        )
    )

    cards = context.driver.find_elements(
        By.XPATH,
        "//h2[contains(text(),'Unlock added value')]/following::a[contains(@href,'circle')]"
    )

    assert len(cards) >= 2, f"Expected at least 2 cards, got {len(cards)}"


@when("Select first product")
def select_first_product(context):
    wait = WebDriverWait(context.driver, 10)

    # wait for results to appear
    wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//a[contains(@href,'/p/')]")
        )
    )


    products = context.driver.find_elements(
        By.XPATH, "//a[contains(@href,'/p/')]"
    )

    products[0].click()

@when("Add product to cart")
def add_to_cart(context):
    wait = WebDriverWait(context.driver, 10)

    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@data-test,'addToCart')]")
        )
    )

    add_button.click()


@then("Verify product is added to cart")
def verify_product_added(context):
    wait = WebDriverWait(context.driver, 10)

    # Open cart
    context.driver.get("https://www.target.com/cart")

    # Verify at least one item exists
    cart_items = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@data-test,'cart-item')]")
        )
    )

    assert len(cart_items) > 0, "Cart is empty"
