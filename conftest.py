import pytest
from utils.driver_factory import get_driver, quit_driver

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    quit_driver(driver)
    