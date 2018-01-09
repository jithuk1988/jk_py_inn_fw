import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time
from pages.home.navigation_page import NavigationPage
from utilities.util import Util

class ResourcePage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    _newButton = ".//div[contains(@id,'resourcenavigation')]//a//span[text()='New']"
    _firstName = ".//input[@name='firstName']"
    _lastName = ".//input[@name='lastName']"
    _unitSelectBox = ".//select[@name='departmentId']"
    """
    select = Select(driver.find_element_by_id('fruits01'))
    # select by visible text
    select.select_by_visible_text('Banana')
    # select by value 
    select.select_by_value('1')
    """
    _immediateSupButton = ".//*[@id='supervisorId_button']"
    _timeAppButton = ".//*[@id='tsApproverId_button']"
    _expAppButton = ".//*[@id='expApproverId_button']"
    _primaryRoleSelectBox = ".//select[@name='primaryRoleId']"
    _supSelection = "//a[text()='Administrator, Innotas']"
    _saveButton = ".//*[@id='getSave']"
    _delLink = ".//div/a/span/span[contains(text(),'Delete')]"
    _delConfirmYes = ".//div/a/span/span/span[text()='Yes']"
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.util = Util()

    def resourceCreation(self,firstName,lastName,primaryRole,unit):
        time.sleep(2)
        self.nav.navigateToResourceTab()
        element1 = self.waitForElement(self._newButton)
        self.elementClick(element=element1)
        time.sleep(1)
        parent_handler = self.driver.current_window_handle
        handlers = []
        current_window=''
        handlers.append(parent_handler)
        current_window_index = len(handlers)-1
        for handles in self.driver.window_handles:
            if handles not in handlers:
                current_window=handles
                break

        handlers.append(current_window)
        self.driver.switch_to_window(current_window)
        current_window_index = len(handlers) - 1
        #handlers.append(self.driver.current_window_handle)
        print(handlers)
        self.driver.implicitly_wait(4)
        self.sendKeys(firstName,locator=self._firstName)
        self.sendKeys(lastName,locator=self._lastName)
        self.elementClick(self._immediateSupButton)
        self.driver.implicitly_wait(4)
        for handles in self.driver.window_handles:
            if handles not in handlers:
                current_window = handles
                break
        handlers.append(current_window)
        current_window_index = len(handlers) - 1
        self.driver.switch_to_window(current_window)
        self.elementClick(self._supSelection)
        handlers.pop()
        current_window_index = len(handlers) - 1
        self.driver.switch_to_window(handlers[current_window_index])
        self.elementClick(self._timeAppButton)
        self.driver.implicitly_wait(4)
        for handles in self.driver.window_handles:
            if handles not in handlers:
                current_window = handles
                break
        handlers.append(current_window)
        self.driver.switch_to_window(current_window)
        self.elementClick(self._supSelection)
        handlers.pop()
        current_window_index = len(handlers) - 1
        self.driver.switch_to_window(handlers[current_window_index])
        self.elementClick(self._expAppButton)
        self.driver.implicitly_wait(4)
        for handles in self.driver.window_handles:
            if handles not in handlers:
                current_window = handles
                break
        handlers.append(current_window)
        self.driver.switch_to_window(current_window)
        self.elementClick(self._supSelection)
        handlers.pop()
        current_window_index = len(handlers) - 1
        self.driver.switch_to_window(handlers[current_window_index])
        self.driver.implicitly_wait(5)
        self.listSelection(locator=self._primaryRoleSelectBox, visibleText=primaryRole)
        self.driver.implicitly_wait(5)
        self.listSelection(locator=self._unitSelectBox, visibleText=unit)
        self.elementClick(locator=self._saveButton)
        self.driver.implicitly_wait(4)
        user_alert = self.driver.switch_to_alert()
        print(user_alert.text)
        user_alert.dismiss()
        self.driver.switch_to_window(handlers[0])
        resName = lastName+", "+firstName
        exp_path = ".//table/tbody/tr/td/div[contains(text(),'"+resName+"')]"
        result = self.isElementPresent(locator=exp_path,locatorType="xpath")
        return result

    def ResourceDeletion(self, firstName, lastName):
        self.nav.navigateToResourceTab()
        resName = lastName + ", " + firstName
        exp_path = ".//table/tbody/tr/td/div[contains(text(),'" + resName + "')]"
        self.driver.implicitly_wait(4)
        self.rightClick(exp_path)
        self.driver.implicitly_wait(2)
        self.elementClick(locator=self._delLink)
        self.elementClick(locator=self._delConfirmYes)
        self.driver.implicitly_wait(4)
        self.driver.refresh()
        self.driver.implicitly_wait(15)
        result = self.isElementPresent(locator=exp_path, locatorType="xpath")
        return not result