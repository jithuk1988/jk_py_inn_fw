from pages.login.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TCStatus
from configfiles.dbconnection import MyDatabase
from configfiles.dbconnection import DbMethods
import datetime

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginAction = LoginPage(self.driver)
        self.testreults = TCStatus(self.driver)
    @pytest.mark.run(order=3)
    def testValidLogin(self):
        testName = 'Valid Login Search Box Verification'
        start = datetime.datetime.now()
        self.loginAction.navigateTo(self.loginAction._loginpage_url)
        self.loginAction.login("v5auto","innotas")
        actualresult1 = self.loginAction.verifyLoginSuccess()
        self.testreults.mark(actualresult1,testName)
        # actualresult2 = self.loginAction.verifyFooterLogo()
        # self.testreults.markFinal("Login Test",actualresult1, "Valid Login Test-Footer Image")
        end = datetime.datetime.now()
        dbMeth=DbMethods()
        timeTaken = dbMeth.timeDiff(start,end)
        insertqry=dbMeth.queryTestInsert(testname=testName,start=start,end=end,result=actualresult1,time=timeTaken)
        db=MyDatabase()
        db.query(insertqry)
        db.close()
    @pytest.mark.run(order=2)
    def testInvalidLogin(self):
        testName = "Invalid Login Test"
        start = datetime.datetime.now()
        self.loginAction.navigateTo(self.loginAction._loginpage_url)
        self.loginAction.login("v5auto", "innotas21")
        actualresult = self.loginAction.verifyFailedLogin()
        self.testreults.markFinal(testName,actualresult, "Invalid Login Test")
        end = datetime.datetime.now()
        dbMeth = DbMethods()
        timeTaken = dbMeth.timeDiff(start, end)
        insertqry = dbMeth.queryTestInsert(testname=testName, start=start, end=end, result=actualresult,
                                           time=timeTaken)
        db = MyDatabase()
        db.query(insertqry)
        db.close()
    @pytest.mark.run(order=1)
    def testLoginPageTitle(self):
        testName = "Login Page Title Verification Test"
        start = datetime.datetime.now()
        actualresult = self.loginAction.verifyLoginPageTitle()
        self.testreults.mark(actualresult, "Login Page Title Test")
        end = datetime.datetime.now()
        dbMeth = DbMethods()
        timeTaken = dbMeth.timeDiff(start, end)
        insertqry = dbMeth.queryTestInsert(testname=testName, start=start, end=end, result=actualresult,
                                           time=timeTaken)
        db = MyDatabase()
        db.query(insertqry)
        db.close()