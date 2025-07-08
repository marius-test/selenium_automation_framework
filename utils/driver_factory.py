from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import config


def get_driver(headless=config.HEADLESS):
    options = Options()
    
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")  # recommended for headless Chrome
        options.add_argument("--window-size=1920,1080")  # optional: set window size for headless
    
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def quit_driver(driver):
    if driver:
        driver.quit()
