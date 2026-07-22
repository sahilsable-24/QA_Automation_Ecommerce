import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.open()
    return login_page
    