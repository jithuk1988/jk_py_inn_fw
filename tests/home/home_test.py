from pages.home.home_page import HomePage
import unittest
import pytest
from utilities.teststatus import TCStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class HomeTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.homeActions = HomePage(self.driver)
        self.testreults = TCStatus(self.driver)

    @pytest.mark.run(order=1)
    def testAdminNavigation(self):
        actualresult=self.homeActions.verifyAdminPageNavgation()
        print(actualresult)
        self.testreults.markFinal("Admin Navigation", actualresult, "Navigate to Admin Page")




