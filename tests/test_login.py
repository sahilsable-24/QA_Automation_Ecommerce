from playwright.sync_api import Page
from pages.login_page import LoginPage


# def test_open_saucedemo(page:Page):
#     page.goto("https://www.saucedemo.com")
#     # assert page.title() == "Swag Labs"

def test_login (page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com")
    login_page.login("standard_user", "secret_sauce")
    assert page.locator(".title").inner_text() == "Products"

def test_invalid_login(page):
    login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com")
    login_page.login("wrong_user", "wrong_pass")
    assert "do not match" in login_page.get_error_message()    
