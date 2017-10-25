from pages.project.project_page import ProjectPage
import unittest
import pytest
from utilities.teststatus import TCStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class HomeTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.projectActions = ProjectPage(self.driver)
        self.testreults = TCStatus(self.driver)

    @pytest.mark.run(order=1)
    def testProjectNew(self):
        actualresult=self.projectActions.verifyProjectCreation()
        print(actualresult)
        self.testreults.markFinal("Project New", actualresult, "Project New Tab")




