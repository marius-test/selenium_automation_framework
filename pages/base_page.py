# optional utility methods are commented out below.
# uncomment as test coverage expands and reuse is needed.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # -------------------------------
    # common element interaction
    # -------------------------------
      
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        self.find(locator).click()
        
    def type(self, locator, text):
        self.find(locator).clear()
        self.find(locator).send_keys(text)
        
    def get_text(self, locator):
        return self.find(locator).text

    # -------------------------------
    # optional utilities (commented out)
    # -------------------------------

    # def find_all(self, locator):
    #     return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    # def is_visible(self, locator):
    #     try:
    #         return self.wait.until(EC.visibility_of_all_element_located(locator))
    #     except:
    #         return False
        
    # def is_clickable(self, locator):
    #     try:
    #         return self.wait.until(EC.element_to_be_clickable(locator))
    #     except:
    #         return False
        
    # def wait_for_disappear(self, locator, timeout=10):
    #     WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))
        
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
    #     self.wait.until(EC.alert_is_present())
    #     self.driver.switch_to.alert.accept()
        
    # def dismiss_alert(self):
    #     self.wait.until(EC.alert_is_present())
    #     self.driver.switch_to.alert.dismiss()
