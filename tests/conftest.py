import pytest
from base.webdriverfactory import WebDriverFactory
import time
import utilities.custom_logger as cl
import logging
from pages.login.login_page import LoginPage
from pages.home.navigation_page import NavigationPage
from utilities.util import Util

log = cl.customLogger(logging.DEBUG)
util=Util()

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
    lp=LoginPage(driver)
    nav = NavigationPage(driver)
    lp.login("v5auto","innotas")
    util.sleep(30,"Home Page Cache Load")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    nav.logout()
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