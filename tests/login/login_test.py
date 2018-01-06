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
    @pytest.mark.run(order=3)
    def testValidLogin(self):
        self.loginAction.navigateTo(self.loginAction._loginpage_url)
        self.loginAction.login("v5auto","innotas")
        actualresult1 = self.loginAction.verifyLoginSuccess()
        self.testreults.mark(actualresult1,"Valid Login Test-Search Box")
        actualresult2 = self.loginAction.verifyFooterLogo()
        self.testreults.markFinal("Login Test",actualresult2, "Valid Login Test-Footer Image")

    @pytest.mark.run(order=2)
    def testInvalidLogin(self):
        self.loginAction.navigateTo(self.loginAction._loginpage_url)
        self.loginAction.login("v5auto", "innotas21")
        actualresult = self.loginAction.verifyFailedLogin()
        self.testreults.markFinal("Invalid Login Test ",actualresult, "Invalid Login Test")

    @pytest.mark.run(order=1)
    def testLoginPageTitle(self):
        actualresult = self.loginAction.verifyLoginPageTitle()
        self.testreults.mark(actualresult, "Login Page Title Test")
