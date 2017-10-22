import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from utilities.util import Util

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    util = Util()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _nav_userdropdown = "//div[contains(@id,'toolbar')]/div[contains(@id,'toolbar')]/a[contains(@id,'splitbutton') and contains(@class,'user-toolbar-button')]/span[contains(@aria-labelledby,'splitbutton')]"
    _nav_home = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Home']"
    _nav_org = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Organization(dd)']"
    _nav_port = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Portfolio I']"
    _nav_acc = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Accounts']"
    _nav_req = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Requests']"
    _nav_proj = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Projects(dd)']"
    _nav_iss = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Issues(dd)']"
    _nav_res = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Resources(dd)']"
    _nav_ppa = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='PPA']"
    _nav_rep = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Reports']"
    _nav_dash = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Dashboards(dd)']"
    _nav_admin = ".//div[contains(@id,navtoolbar)]/div[contains(@id,navtoolbar)]/a[@aria-label='Admin']"
    _logout_link = ".//a/span[text()='Logout']"

    def navigateToHomeTab(self):
        self.elementClick(locator=self._nav_home)


    def navigateToOrgTab(self):
        self.elementClick(locator=self._nav_org)

    def navigateToPortfolioTab(self):
        self.elementClick(locator=self._nav_port)

    def navigateToAccountTab(self):
        self.elementClick(locator=self._nav_acc)

    def navigateToRequestTab(self):
        self.elementClick(locator=self._nav_req)

    def navigateToProjectTab(self):
        self.elementClick(locator=self._nav_proj)

    def navigateToIssueTab(self):
        self.elementClick(locator=self._nav_iss)

    def navigateToResourceTab(self):
        self.elementClick(locator=self._nav_res)

    def navigateToPPATab(self):
        self.elementClick(locator=self._nav_ppa)

    def navigateToReportTab(self):
        self.elementClick(locator=self._nav_rep)

    def navigateToDashboardTab(self):
        self.elementClick(locator=self._nav_dash)

    def navigateToAdminTab(self):
        self.elementClick(locator=self._nav_admin)

    def navigateToUserSettings(self):
        self.splitButtonClick(locator=self._nav_userdropdown,
                                      locatorType="xpath")
        #self.elementClick(locator=self._nav_userdropdown)

    def logout(self):
        self.util.sleep(sec=4,info="Waiting 4 Seconds before Logging out..")
        self.navigateToUserSettings()
        self.util.sleep(sec=2)
        self.elementClick(self._logout_link)
