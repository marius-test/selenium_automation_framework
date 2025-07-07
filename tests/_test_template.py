import unittest
from time import sleep

import urllib3
import requests
import pyautogui
from pynput.keyboard import Key, Controller

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from utils.driver_factory import (
    get_driver, 
    quit_driver,
)
from utils.waits import (
    wait_for_presence,
)
from seletools.actions import drag_and_drop

# TEST DATA
URL = "https://the-internet.herokuapp.com"
