# optional utility methods are commented out below.
# uncomment as test coverage expands and reuse is needed.

# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains

from utils.waits import (
    wait_for_presence,
    # wait_for_all_presence,
    # wait_for_visibility,
    # wait_for_clickable,
    # wait_for_invisibility,
    # wait_for_alert,
)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # -------------------------------
    # common element interaction
    # -------------------------------
    
    def open(self, url=None):
        if url is None:
            if hasattr(self, "URL"):
                url = self.URL
            else:
                raise ValueError("URL must be provided or set as 'URL' attribute on the page.")
        self.driver.get(url)
      
    def find(self, locator):
        return wait_for_presence(self.driver, locator)
    
    def click(self, locator):
        self.find(locator).click()
        
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):
        return self.find(locator).text

    # -------------------------------
    # optional utilities (commented out)
    # -------------------------------

    # def find_all(self, locator):
    #     return wait_for_all_presence(self.driver, locator)
    
    # def is_visible(self, locator):
    #     try:
    #         return wait_for_visibility(self.driver, locator)
    #     except:
    #         return False
        
    # def is_clickable(self, locator):
    #     try:
    #         return wait_for_clickable(self.driver, locator)
    #     except:
    #         return False
        
    # def wait_for_disappear(self, locator, timeout=10):
    #     wait_for_invisibility(self.driver, locator)
        
    # def select_by_invisible_text(self, locator, text):
    #     select = Select(self.find(locator))
    #     select.select_by_visible_text(text)
        
    # def hover(self, locator):
    #     element = self.find(locator)
    #     ActionChains(self.driver).move_to_element(element).perform()
        
    # def get_attribute(self, locator, attribute):
    #     return self.find(locator).get_attribute(attribute)
    
    # def get_value(self, locator):
    #     return self.find(locator).get_attribute("value")
    
    # def get_title(self):
    #     return self.driver.title
    
    # def get_current_url(self):
    #     return self.driver.current_url
    
    # def refresh_page(self):
    #     self.driver.refresh()
        
    # def accept_alert(self):
    #     wait_for_alert(self.driver)
    #     self.driver.switch_to.alert.accept()
        
    # def dismiss_alert(self):
    #     wait_for_alert(self.driver)
    #     self.driver.switch_to.alert.dismiss()
