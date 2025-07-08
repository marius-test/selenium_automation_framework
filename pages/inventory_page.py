from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import INVENTORY_URL


class InventoryPage(BasePage):
    URL = INVENTORY_URL

    APP_LOGO = (By.CLASS_NAME, "app_logo")
    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    