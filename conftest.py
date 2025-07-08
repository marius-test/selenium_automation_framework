import pytest
from datetime import datetime
from utils.driver_factory import get_driver, quit_driver

@pytest.fixture(scope="function")
def driver(request):
    # setup: create a new driver instance
    driver = get_driver()
    yield driver
    
    # teardown: if test failed, save screenshot
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = request.node.name
        filename = f"screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(filename)
        print(f"\nScreenshot saved to {filename}")
        
    # quit the driver at the end
    quit_driver(driver)


# hook to get test result info so fixture can detect failures
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# pytest hook to configure logging before tests run
# sets a timestamped log file name to avoid overwriting previous logs
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    logfile = f"logs/test_{timestamp}.log"
    config.option.log_file = logfile
