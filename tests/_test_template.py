import pytest
from time import sleep

from config import BASE_URL  # import the url/test data you need
from utils.waits import wait_for_presence  # import just the wait(s) you need
from pages.base_page import BasePage  # import page object or base utilities


def test_example(driver):
    """
    Example test: Open URL, wait for presence of element, perform simple assertion.
    """
    
    page = BasePage(driver)  # wrap the driver in the page object
    
    page.open(BASE_URL)   # calls BasePage.open() with the URL

    # example: wait for an element (replace with actual selector and function)
    # wait_for_presence(driver, locator, TIMEOUT)
    
    # base_page.do_something()

    sleep(1)  # placeholder for demo purposes

    assert True  # replace with real assertions
