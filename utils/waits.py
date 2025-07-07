from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

DEFAULT_TIMEOUT = 5

# presence-based waits
def wait_for_presence(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until at least one element is present in the DOM."""
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def wait_for_all_presence(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until all elements matching locator are present in the DOM."""
    return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(locator))

# visibility-based waits
def wait_for_visibility(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until element is visible (present and visible)."""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_for_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until element is visible and enabled for clicking."""
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

# invisibility wait
def wait_for_invisibility(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Wait until element is no longer visible or not present."""
    return WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))

# wait for alert
def wait_for_alert(driver, timeout=DEFAULT_TIMEOUT):
    """Wait until a browser alert is present."""
    return WebDriverWait(driver, timeout).until(EC.alert_is_present())

# generic safe wait with timeout handling
def safe_wait(driver, condition, timeout=DEFAULT_TIMEOUT):
    """Wait for a custom condition, returning None on timeout instead of raising."""
    try:
        return WebDriverWait(driver, timeout).until(condition)
    except TimeoutException:
        print("Timeout while waiting.")
        return None
