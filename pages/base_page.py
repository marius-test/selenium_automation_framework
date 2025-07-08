from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from utils.waits import (
    wait_for_presence,
    wait_for_all_presence,
    wait_for_visibility,
    wait_for_clickable,
    wait_for_invisibility,
    wait_for_alert,
)


class BasePage:
    # ---------------------------
    # common locators used on multiple pages
    # ---------------------------
    TITLE = (By.CLASS_NAME, "title")
    FOOTER = (By.ID, "footer")

    def __init__(self, driver):
        """
        Initialize BasePage with Selenium WebDriver instance.
        """
        self.driver = driver

    # ---------------------------
    # navigation methods
    # ---------------------------
    def open(self, url=None):
        """
        Open a URL in the browser.
        If url is None, attempts to use self.URL attribute.
        """
        if url is None:
            if hasattr(self, "URL"):
                url = self.URL
            else:
                raise ValueError("URL must be provided or set as 'URL' attribute on the page.")
        self.driver.get(url)

    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()

    def get_current_url(self):
        """Return the current browser URL."""
        return self.driver.current_url

    def get_browser_title(self):
        """
        Return the browser tab title (from the <title> tag).
        """
        return self.driver.title

    # ---------------------------
    # element finding methods
    # ---------------------------
    def find(self, locator):
        """
        Find a single element using an explicit wait for presence.
        """
        return wait_for_presence(self.driver, locator)

    def find_all(self, locator):
        """
        Find all elements matching locator using an explicit wait.
        """
        return wait_for_all_presence(self.driver, locator)

    def is_visible(self, locator):
        """
        Return True if element is visible, else False.
        """
        try:
            return wait_for_visibility(self.driver, locator)
        except:
            return False

    def is_clickable(self, locator):
        """
        Return True if element is clickable, else False.
        """
        try:
            return wait_for_clickable(self.driver, locator)
        except:
            return False

    # ---------------------------
    # element interaction methods
    # ---------------------------
    def click(self, locator):
        """
        Click an element after waiting for its presence.
        """
        self.find(locator).click()

    def type(self, locator, text):
        """
        Clear a text field and type the given text.
        """
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def hover(self, locator):
        """
        Hover mouse pointer over the element.
        """
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_by_visible_text(self, locator, text):
        """
        Select an option from a dropdown by visible text.
        """
        select = Select(self.find(locator))
        select.select_by_visible_text(text)

    # ---------------------------
    # getters for element attributes and text
    # ---------------------------
    def get_text(self, locator):
        """
        Return the text content of an element.
        """
        return self.find(locator).text

    def get_attribute(self, locator, attribute):
        """
        Return the value of a given attribute for the element.
        """
        return self.find(locator).get_attribute(attribute)

    def get_value(self, locator):
        """
        Return the 'value' attribute of an element.
        """
        return self.get_attribute(locator, "value")

    # ---------------------------
    # wait helpers
    # ---------------------------
    def wait_for_disappear(self, locator, timeout=10):
        """
        Wait until an element becomes invisible or disappears.
        """
        wait_for_invisibility(self.driver, locator, timeout=timeout)

    # ---------------------------
    # alert handling
    # ---------------------------
    def accept_alert(self):
        """
        Wait for an alert and accept it.
        """
        wait_for_alert(self.driver)
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Wait for an alert and dismiss it.
        """
        wait_for_alert(self.driver)
        self.driver.switch_to.alert.dismiss()
