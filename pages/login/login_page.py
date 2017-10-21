from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Page Locators
    _username_textbox = "login" # ID
    _password_textbox = "password" # Name
    _login_button = ".//*[@id='UserPassForm']/form/button" # XPath

    def enterUsername(self,username):
        self.sendKeys(username,self._username_textbox,locatorType="id")

    def enterPassword(self,password):
        self.sendKeys(password, self._password_textbox, locatorType="name")

    def clickLogin(self):
        self.elementClick(self._login_button)

    def login(self,username,password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLogin()

    def verifyLoginSuccess(self):
        result=self.isWaitedElementPresent(".//input[@name='searchText']",timeout=20)
        return result

    def verifyFailedLogin(self):
        result=self.isWaitedElementPresent("login-error-msg",
                                     locatorType="class")
        return result

    def verifyFooterLogo(self):
        result=self.isWaitedElementPresent(".//img[@src='/image/ttlogos/powered_by_logo.png' and @alt='Powered by Innotas']",
                                           timeout=20)
        return result