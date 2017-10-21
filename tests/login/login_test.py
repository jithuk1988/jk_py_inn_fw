from selenium import webdriver
from pages.login.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TCStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginAction = LoginPage(self.driver)
        self.testreults = TCStatus(self.driver)

    @pytest.mark.run(order=2)
    def testValidLogin(self):
        self.loginAction.login("v5new6auto","innotas")
        actualresult1 = self.loginAction.verifyLoginSuccess()
        self.testreults.mark(actualresult1,"alid Login Test-Search Box")
        actualresult2 = self.loginAction.verifyFooterLogo()
        self.testreults.markFinal("Login Test",actualresult2, "Valid Login Test-Footer Image")

    @pytest.mark.run(order=1)
    def testInvalidLogin(self):
        self.loginAction.login("v5new6auto", "innotas21")
        actualresult = self.loginAction.verifyFailedLogin()
        self.testreults.markFinal("Login Test", actualresult, "Invalid Login Test")
        assert actualresult == True