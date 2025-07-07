from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import LOGIN_URL


class LoginPage(BasePage):
    URL = LOGIN_URL
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error-message-container.error > h3")
    
    
    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)
