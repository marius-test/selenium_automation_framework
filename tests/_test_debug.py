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
from webdriver_manager.chrome import ChromeDriverManager

PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
# driver = webdriver.Chrome(service=PATH)
driver = webdriver.Chrome(ChromeDriverManager().install())

# action_chains = ActionChains(driver)
# alert = Alert(driver)

url = "https://www.saucedemo.com/"

if __name__ == '__main__':
    unittest.main()
