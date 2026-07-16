from playwright.sync_api import Page


def test_open_saucedemo(page:Page):
    page.goto("https://www.saucedemo.com")
    assert page.title() == "Swag Labs"

