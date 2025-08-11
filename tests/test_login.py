import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config import (
    STANDARD_USER,
    LOCKED_OUT_USER,
    PROBLEM_USER,
    PERFORMANCE_GLITCH_USER,
    ERROR_USER,
    VISUAL_USER,
    PASSWORD,
)


# positive test: users should be able to log in
@pytest.mark.parametrize("username", [
    STANDARD_USER,
    PROBLEM_USER,
    PERFORMANCE_GLITCH_USER,
    VISUAL_USER,
])
def test_successful_login_variants(driver, username):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_text(inventory_page.TITLE) == "Products", f"{username} login failed unexpectedly"


# negative test: users should *not* be able to log in
@pytest.mark.parametrize("username", [
    LOCKED_OUT_USER,
    ERROR_USER,
])
def test_login_should_fail(driver, username):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, PASSWORD)

    assert login_page.is_error_displayed()
    