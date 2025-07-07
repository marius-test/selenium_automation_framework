import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# <========== TEST CASES STARTS HERE ==========>

import unittest
import requests

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence

# TEST DATA
URL = "https://www.saucedemo.com/"

# <========== TEST CASES ENDS HERE ==========>


if __name__ == "__main__":
    print("It works!")
