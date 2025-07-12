from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import INVENTORY_URL


class InventoryPage(BasePage):
    URL = INVENTORY_URL

    # locators
    APP_LOGO = (By.CSS_SELECTOR, "#header_container .app_logo")
    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    FILTER_DROPDOWN = (By.CSS_SELECTOR, "#header_container .product_sort_container")
    ACTIVE_FILTER = (By.CSS_SELECTOR, "#header_container .active_option")
    CART_BUTTON = (By.CSS_SELECTOR, "#shopping_cart_container > a")
    
    # available filter options
    FILTER_OPTIONS = [
        "Name (A to Z)",
        "Name (Z to A)",
        "Price (low to high)",
        "Price (high to low)",
    ]

    def select_filter(self, option_text: str):
        """
        Select a filter option from the dropdown by visible text.
        Raises:
            ValueError: If the filter text is not in FILTER_OPTIONS.
        """
        if option_text not in self.FILTER_OPTIONS:
            raise ValueError(f"Invalid filter option: {option_text}. Must be one of: {self.FILTER_OPTIONS}")
        
        self.select_by_visible_text(self.FILTER_DROPDOWN, option_text)
        
    def get_active_filter_text(self) -> str:
        """
        Get currently selected filter label (from the active_option span).
        """
        return self.get_text(self.ACTIVE_FILTER)
