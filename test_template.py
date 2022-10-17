# delete unused imports
import time
import unittest
import urllib3
import requests
import pyautogui
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
# driver = webdriver.Chrome(service=PATH)
# action_chains = ActionChains(driver)
# alert = Alert(driver)
# test data here


class TestName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
    
    def test_x(self):
        driver = self.driver
        # locators, waits, actions here
        self.assertEqual(1, 1)
    
    def test_y(self):
        driver = self.driver
        # locators, waits, actions here
        self.assertEqual(1, 1)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()