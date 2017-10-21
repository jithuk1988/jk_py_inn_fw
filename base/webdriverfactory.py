"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Download all browser drivers and set the path in Environment variables in order to invoke all 
        browser diver using single command.
        
        Otherwise use the below method
        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        *PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://q3.innotas.io"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
            # Maximize the window
            driver.maximize_window()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            # Maximize Not required for firefox because its defaults to Maximized mode- Command cause minimize
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
            # Maximize the window
            driver.maximize_window()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Loading browser with App URL
        driver.get(baseURL)
        return driver