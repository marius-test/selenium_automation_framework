import sys
import os

# add root project path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from config import BASE_URL
from pages.base_page import BasePage
from utils.waits import wait_for_presence


# <========== TEST CASES ENDS HERE ==========>

@pytest.mark.headless(True)
def test_debug(driver):
    page = BasePage(driver)
    page.open(BASE_URL)
    
    assert True == False
    
# <========== TEST CASES ENDS HERE ==========>


if __name__ == "__main__":
    pytest.main([__file__])
