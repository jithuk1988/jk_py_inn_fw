from pages.project.project_page import ProjectPage
import unittest
import pytest
from utilities.teststatus import TCStatus
from ddt import ddt,data,unpack

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class ProjectTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.projectActions = ProjectPage(self.driver)
        self.testreults = TCStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("Auto Category","10/17/2017","Auto Project 002", "01/01/2017", "12/31/2017","In Progress"))
    def testProjectNew(self,category,scheduleDate,title,startDate,targetDate,status):
        actualresult=self.projectActions.verifyProjectCreation(category=category,scheduleDate=scheduleDate,title=title,startDate=startDate, targetDate=targetDate,status=status)
        #print(actualresult)
        self.testreults.markFinal("Project New", actualresult, "Project New Tab")




