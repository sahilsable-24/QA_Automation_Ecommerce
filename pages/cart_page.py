from pages.base_page import BasePage

class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.cart_item = self.page.locator(".cart_item")
        self.checkout_button = self.page.locator("button", has_text="Checkout")

    def get_item_count(self):
        return self.cart_item.count()

    def get_item_names(self):
        return self.page.locator(".inventory_item_name").all_inner_texts()

    def start_checkout(self):
        self.checkout_button.click()

    def remove_item_by_item_name(self, product_name):
        item = self.page.locator(".cart_item", has_text=product_name)
        item.locator("button", has_text="Remove").click()