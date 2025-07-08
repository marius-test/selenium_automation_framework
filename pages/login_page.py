from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import LOGIN_URL


class LoginPage(BasePage):
    URL = LOGIN_URL
    
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error-message-container.error > h3")
    ERROR_CLOSE_BUTTON = (By.CSS_SELECTOR, "div.error-message-container.error button")

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def close_error_message(self):
        self.click(self.ERROR_CLOSE_BUTTON)
    
    def login_logo_text(self):
        return self.get_text(self.LOGIN_LOGO)
    
    def get_username_placeholder(self):
        return self.find(self.USERNAME_INPUT).get_attribute("placeholder")

    def get_password_placeholder(self):
        return self.find(self.PASSWORD_INPUT).get_attribute("placeholder")
    
    def get_login_button_text(self):
        return self.find(self.LOGIN_BUTTON).get_attribute("value")
