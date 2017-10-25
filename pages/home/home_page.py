import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
from pages.home.navigation_page import NavigationPage
from utilities.util import Util


class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    _adminOrgLink = "Organization(dd)"   #Link text

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.util = Util()

    def verifyAdminPageNavgation(self):
        self.nav.navigateToAdminTab()

        adminPageText=self.getText(self._adminOrgLink,locatorType="link")
        result = self.util.verifyTextMatch(adminPageText,"Organization(dd)")
        return result
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

