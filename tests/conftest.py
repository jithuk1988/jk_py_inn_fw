import pytest
from base.webdriverfactory import WebDriverFactory
import time
import utilities.custom_logger as cl
import logging

log = cl.customLogger(logging.DEBUG)

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    #Running one time setUp
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    log.info("Quiting browser in 3 Seconds")
    time.sleep(3)
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")

def osType(request):
    return request.config.getoption("--osType")