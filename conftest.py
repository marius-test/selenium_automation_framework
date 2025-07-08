import pytest
from datetime import datetime
from utils.driver_factory import get_driver, quit_driver

@pytest.fixture(scope="function")  # runs setup and teardown for each test function separately to ensure clean state per test and avoids side effects
def driver(request):
    # get headless value from test marker or use default (False)
    headless = getattr(request.node, "headless", False)

    # setup: create a new driver instance
    driver = get_driver(headless=headless)
    yield driver

    # teardown: if test failed, save screenshot
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = request.node.name
        filename = f"screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(filename)
        print(f"\nScreenshot saved to {filename}")

    # quit the driver
    quit_driver(driver)


# hook to detect test results so the fixture knows if a test failed
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# hook to capture the "headless" marker from tests
def pytest_runtest_setup(item):
    headless_marker = item.get_closest_marker("headless")
    if headless_marker:
        item.headless = headless_marker.args[0]
    else:
        item.headless = False


# hook to configure logging dynamically
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    logfile = f"logs/test_{timestamp}.log"
    config.option.log_file = logfile
