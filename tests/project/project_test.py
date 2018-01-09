from pages.project.project_page import ProjectPage
import unittest
import pytest
from utilities.teststatus import TCStatus
from ddt import ddt,data,unpack
from base.selenium_driver import SeleniumDriver

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class ProjectTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.projectActions = ProjectPage(self.driver)
        self.testreults = TCStatus(self.driver)
    """ @data(("Auto Category","10/17/2017","Auto Project 011", "01/01/2017", "12/31/2017","In Progress"),
          ("Auto Category","10/17/2017","Auto Project 012", "01/01/2017", "12/31/2017","In Progress"))
    """

    @pytest.mark.run(order=1)
    @data(*SeleniumDriver.get_csv_data("C:/Python_Workspace/FrameWork/project.csv"))
    @unpack
    def testProjectNew(self,category,scheduleFrmDate,projectTitle,startDate,targetDate,status):
        actualresult=self.projectActions.verifyProjectCreation\
            (category=category,scheduleDate=scheduleFrmDate,title=projectTitle,startDate=startDate, targetDate=targetDate,status=status)
        #print(actualresult)
        self.testreults.markFinal("Project New", actualresult, "Project New Creation")




