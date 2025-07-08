import sys
import os

# add root project path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from config import BASE_URL
from pages.base_page import BasePage
from utils.waits import wait_for_presence


def test_debug(driver):
    page = BasePage(driver)
    page.open(BASE_URL)
    pass

if __name__ == "__main__":
    pytest.main([__file__])
