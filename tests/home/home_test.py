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
    def testHomeNavigation(self):
        self.homeActions.clickTopLinks()



