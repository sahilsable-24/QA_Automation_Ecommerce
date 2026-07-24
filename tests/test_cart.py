from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from data.test_data import USERS

def test_cart_reflects_items_added(login_page):
    login_page.login(USERS["standard"]["username"], USERS["standard"]["password"])
    inventory_page = InventoryPage(login_page.page)
    inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
    inventory_page.go_to_cart()
    cart_page = CartPage(login_page.page)
    assert cart_page.get_item_count() == 2
    assert "Sauce Labs Backpack" in cart_page.get_item_names()

def test_removing_items_in_cart(login_page):
    login_page.login(USERS["standard"]["username"], USERS["standard"]["password"])
    inventory_page = InventoryPage(login_page.page)
    inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
    inventory_page.go_to_cart()
    cart_page = CartPage(login_page.page)
    product_name = "Sauce Labs Backpack"
    cart_page.remove_item_by_item_name(product_name)
    assert cart_page.get_item_count() == 1