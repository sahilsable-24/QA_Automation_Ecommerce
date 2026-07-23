from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import USERS
from data.test_data import PRODUCTS_NAME
import pytest


def test_inventory_shows_6_products(login_page):
    login_page.login(USERS["standard"]["username"], USERS["standard"]["password"])
    inventory_page = InventoryPage(login_page.page)
    assert inventory_page.get_product_count() == 6

@pytest.mark.parametrize("product_name",PRODUCTS_NAME)
def test_add_and_remove_products_updates_cart_badge(login_page, product_name):
    login_page.login(USERS["standard"]["username"], USERS["standard"]["password"])
    inventory_page = InventoryPage(login_page.page)
    inventory_page.add_product_to_cart_by_name(product_name)
    # inventory_page.page.screenshot(path="after_click.png")
    print(inventory_page.cart_badge.is_visible())
    assert inventory_page.get_cart_count() == 1
    inventory_page.remove_product_from_cart_by_name(product_name)
    assert inventory_page.cart_badge.is_visible() == False

def test_sort_price_low_to_high(login_page):
    login_page.login(USERS["standard"]["username"], USERS["standard"]["password"])
    inventory_page = InventoryPage(login_page.page)
    option_value = "Price (low to high)"
    inventory_page.sort_products(option_value)
    print(inventory_page.get_active_option())
    print(inventory_page.get_all_prices())
    prices = inventory_page.get_all_prices()
    assert inventory_page.get_active_option() == option_value and prices == sorted(prices)