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
    _scheduleFromDateInput = ".//div[@role='dialog']//input[@name='scheduleFromDate']"
    _projectTitle = ".//div[@role='dialog']//textarea[@name='title']"
    _statusBox = ".//div[@role='dialog']//input[@name='LLStatusId']"
    _statusSelection = ".//ul/div[contains(text(),'dummy')]"
    _startDateInput = ".//div[@role='dialog']//input[@name='startDate']"
    _targetDateInput = ".//div[@role='dialog']//input[@name='targetDate']"
    _saveButton = "//div[@role='dialog']//span[text()='Save']"
    _headerTitle = ".//div[contains(@class,'primaryHeader')]//div[contains(@id,'header-title-textEl')]"
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.util = Util()

    def verifyProjectCreation(self,category, scheduleDate, title, status, startDate, targetDate):
        time.sleep(5)
        self.nav.navigateToProjectTab()
        element1 = self.waitForElement(self._newButton)
        self.elementClick(element=element1)
        time.sleep(1)
        self.clickUsingLabelText("Project Category:")
        time.sleep(5)
        xpath=self.getXpathOfSelectBoxValue(category)
        element2 = self.waitForElement(xpath)
        self.elementClick(element=element2)
        self.sendKeys(scheduleDate,locator=self._scheduleFromDateInput)
        #self.log.info("***********************************************************")
        element3 = self.waitForElement(self._nextButton)
        self.elementClick(element=element3)
        self.sendKeys(title,locator=self._projectTitle)
        self.elementClick(locator=self._statusBox)
        time.sleep(2)
        statusxpath=self._statusSelection.replace("dummy",status)
        print(statusxpath)
        element5 = self.waitForElementToClickable(locator=statusxpath)
        self.elementClick(element=element5)
        self.sendKeys(startDate,locator=self._startDateInput)
        self.sendKeys(targetDate, locator=self._targetDateInput)
        self.elementClick(locator=self._saveButton)
        actualTitle=self.getText(locator=self._headerTitle)
        return actualTitle
        #self.clickUsingLabelTextInDialog("Title")

       # self.sendKeys("Proname-00",element=ele)

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

