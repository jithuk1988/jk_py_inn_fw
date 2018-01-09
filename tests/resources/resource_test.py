from pages.resources.resource_page import ResourcePage
import unittest
import pytest
from utilities.teststatus import TCStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class ResourceTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.resourceActions = ResourcePage(self.driver)
        self.testreults = TCStatus(self.driver)

    @pytest.mark.run(order=1)
    def testResourceNew(self):
        # print(actualresult)
        actualresult=self.resourceActions.resourceCreation(firstName="Hardik",lastName="Pandya",primaryRole="Support",unit="Organization Top Level")
        self.testreults.markFinal("New Resource", actualresult, "Resource created")

    @pytest.mark.run(order=2)
    def testResourceDel(self):
        actualresult = self.resourceActions.ResourceDeletion(firstName="Hardik", lastName="Pandya")
        self.testreults.markFinal("Resource Deletion", actualresult, "Resource Deleted")