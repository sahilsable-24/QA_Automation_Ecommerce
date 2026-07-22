from playwright.sync_api import Page
from pages.login_page import LoginPage
from data.test_data import USERS


# def test_open_saucedemo(page:Page):
#     page.goto("https://www.saucedemo.com")
#     # assert page.title() == "Swag Labs"

def test_login (page,login_page):
    login_page.login(USERS["standard"]["username"], USERS["standard"]["password"])
    assert page.locator(".title").inner_text() == "Products"

def test_invalid_login(login_page):
    login_page.login(USERS["invalid"]["username"],  USERS["invalid"]["password"])
    assert "do not match" in login_page.get_error_message()

def test_locked_user(login_page):
    login_page.login(USERS["locked_out"]["username"],  USERS["locked_out"]["password"])
    assert "locked out" in login_page.get_error_message().lower()

def test_empty_username(login_page):
    login_page.login("", USERS["standard"]["password"])
    assert "username is required" in login_page.get_error_message().lower()

def test_empty_password(login_page):
    login_page.login(USERS["standard"]["username"], "")
    assert "password is required" in login_page.get_error_message().lower()    
