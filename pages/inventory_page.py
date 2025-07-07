from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import INVENTORY_URL


class InventoryPage(BasePage):
    URL = INVENTORY_URL
    
    TITLE = (By.CLASS_NAME, "title")
    
    def get_title(self):
        return self.get_text(self.TITLE)
    