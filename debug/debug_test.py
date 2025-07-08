import sys
import os
import pytest

# add root project path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_factory import get_driver, quit_driver


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    quit_driver(driver)

def test_debug(driver):
    driver.get("https://www.saucedemo.com/")
    # add test steps here
    pass

if __name__ == "__main__":
    pytest.main([__file__])
