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
    INVALID_USER,
    PASSWORD,
    WRONG_PASSWORD,
)


# positive test: users should be able to log in
@pytest.mark.parametrize("username", [
    STANDARD_USER,
    PROBLEM_USER,
    PERFORMANCE_GLITCH_USER,
    VISUAL_USER,
    ERROR_USER,
])
def test_login_success_for_various_users(driver, username):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_text(inventory_page.TITLE) == "Products", f"{username} login failed unexpectedly"


# negative test: users should *not* be able to log in
@pytest.mark.parametrize("username,password", [
    (LOCKED_OUT_USER, PASSWORD),
    (INVALID_USER, PASSWORD),
    (STANDARD_USER, WRONG_PASSWORD),
])
def test_login_failure_for_restricted_users(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    assert login_page.is_error_displayed()
    