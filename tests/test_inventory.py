from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import USERS


def test_inventory_shows_6_products(login_page):
    login_page.login(USERS["standard"]["username"], USERS["standard"]["password"])
    inventory_page = InventoryPage(login_page.page)
    assert inventory_page.get_product_count() == 6

def test_add_products_updates_cart_badge(login_page):
    login_page.login(USERS["standard"]["username"], USERS["standard"]["password"])
    inventory_page = InventoryPage(login_page.page)
    inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    # inventory_page.page.screenshot(path="after_click.png")
    print(inventory_page.cart_badge.is_visible())
    assert inventory_page.get_cart_count() == 1