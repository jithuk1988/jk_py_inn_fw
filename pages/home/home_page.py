import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time


class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    topNavIconsLink = ".//div[contains(@id,'navtoolbar')]/a[contains(@id,'button')]"  #xpath

    def getNavLinks(self):
        return self.getElementList(self.topNavIconsLink)

    def clickTopLinks(self):
        for element in self.getNavLinks():
            self.elementClick(element=element)
            time.sleep(4)
            pageTitle=self.getTitle()
            self.log.info("Navigated to Page: " +pageTitle)

