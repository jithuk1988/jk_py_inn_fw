import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
from pages.home.navigation_page import NavigationPage
from utilities.util import Util


class ProjectPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    _newButton = ".//div[contains(@id,'projectnavigation')]//a//span[text()='New']"   #Link text
    _cancelButton = ".//span[text()='Cancel']"
    _nextButton = ".//a/span/span/span[text()='Next']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.util = Util()

    def verifyProjectCreation(self):
        time.sleep(5)
        self.nav.navigateToProjectTab()
        element1 = self.waitForElement(self._newButton)
        self.elementClick(element=element1)
        time.sleep(5)
        self.clickUsingLabelText("Project Category:")
        time.sleep(5)
        xpath=self.getXpathOfSelectBoxValue("Auto Category")
        element2 = self.waitForElement(xpath)
        t = self.elementClick(element=element2)
        #self.log.info("***********************************************************")
        element3 = self.waitForElement(self._nextButton)
        s = self.elementClick(element=element3)
        if t is s:
            return True
        else:
            return False
"""
    topNavIconsLink = ".//div[contains(@id,'navtoolbar')]/a[contains(@id,'button')]"  #xpath

    def getNavLinks(self):
        return self.getElementList(self.topNavIconsLink)

    def clickTopLinks(self):
        for element in self.getNavLinks():
            self.elementClick(element=element)
            time.sleep(4)
            pageTitle=self.getTitle()
            self.log.info("Navigated to Page: " +pageTitle)

"""

