from behave import when, then

from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.health_popup import HealthPopup


@when('Search for "{product_name}"')
def search_for_product(context, product_name):

    popup = HealthPopup(context.driver)
    popup.close_popup()

    search_page = SearchPage(context.driver)

    search_page.search_product(product_name)


@when('Open first product')
def open_first_product(context):

    search_page = SearchPage(context.driver)

    search_page.open_first_product()


@when('Add product to cart')
def add_product_to_cart(context):

    product_page = ProductPage(context.driver)

    product_page.add_to_cart()


@then('Verify cart updated')
def verify_cart_updated(context):

    cart_page = CartPage(context.driver)

    cart_page.verify_cart_updated()