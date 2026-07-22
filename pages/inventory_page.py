from pages.base_page import BasePage
from playwright.sync_api import expect

class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page_title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_product_count(self):
        return self.inventory_items.count()

    def add_product_to_cart_by_name(self,product_name):
        item = self.page.locator(".inventory_item", has_text=product_name)
        # print("Matching items found:", item.count())
        # print("Button text:", item.locator("button").inner_text())
        item.locator("button", has_text="Add to cart").click()

    def get_cart_count(self):
        if self.cart_badge.count == 0:
            return 0
        expect(self.cart_badge).to_be_visible()
        return int(self.cart_badge.inner_text())