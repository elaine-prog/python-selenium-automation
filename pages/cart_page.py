from pages.base_page import Page


class CartPage(Page):

    def open_cart(self):
        self.driver.get("https://www.target.com/cart")

    def verify_empty_cart(self):
        assert "cart" in self.driver.current_url.lower()