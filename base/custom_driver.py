from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os
from selenium.webdriver import ActionChains
from base.selenium_driver import SeleniumDriver


class CustomDriver(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def getXpathOfLabelName(self,label):
        """
        To get the xpath of an element within a page
        :param label:
        :return xpath:
        """
        xpath = "//span[text()='"+label+"']"
        return xpath

    def getXpathOfDialogLabelName(self,label):
        """
        To get the xpath of an element within a dialog Eg: Project Creation dialog
        :param label:
        :return xpath:
        """
        xpath = "//div[@role='dialog']//span[text()='"+label+"']"

    def getXpathOfSelectBoxValue(self,valuetoselect):
        xpath = "//ul/div[contains(text(),'"+valuetoselect+"')]"
        xpat="QA***********************************************************"
        return xpath

    def test(self):
        q = ".//div[@role='dialog']//span/span/span[not(contains(@class,'entity'))]"
        s = ".//div[@role='dialog']//div/div/div[contains(@class,'x-form-text-wrap') and contains(@data-ref,'inputWrap')]"

    def getLabelElement(self, label):
        element=self.getElement(self.getXpathOfLabelName(label))
        return element

    def getDialogLabelElement(self, label):
        element=self.getElement(self.getXpathOfDialogLabelName(label))
        return element

    def rightClick(self, locator="", locatorType = "xpath"):
        try:
            actions = ActionChains(self.driver)
            element = self.waitForElementToClickable(locator,locatorType)
            #elementID=self.getElementID(locator,locatorType)
            actions.move_to_element(element)
            actions.context_click(element)
            actions.perform()
            self.log.info("Right Clicked on Element with locator: " + locator + " and locator Type: " + locatorType)
        except:
            self.log.info("Cannot right click on Element with locator: " + locator + " and locator Type: " + locatorType)
            print_stack()

    def splitButtonClick(self, locator="", locatorType = "xpath"):
        try:
            actions = ActionChains(self.driver)
            element = self.waitForElementToClickable(locator,locatorType)
            #elementID=self.getElementID(locator,locatorType)
            actions.move_to_element(element)
            actions.click(element)
            actions.perform()
            #script="document.getElementById(\""+ elementID + "\").click();"
            #self.driver.execute_script(script)
            #self.log.info(script)
            self.log.info("Clicked on Element with locator: " + locator + " and locator Type: " + locatorType)
        except:
            self.log.info("Cannot click on Element with locator: " + locator + " and locator Type: " + locatorType)
            print_stack()
    def clickUsingLabelText(self, label):
        try:
            actions = ActionChains(self.driver)
            element = self.getLabelElement(label)
            #elementID=self.getElementID(locator,locatorType)
            actions.move_to_element(element)
            actions.click(element)
            actions.perform()
            #script="document.getElementById(\""+ elementID + "\").click();"getDialogLabelElement
            #self.driver.execute_script(script)
            #self.log.info(script)
            self.log.info("Clicked on Element with locator: " + label + " and locator Type: ")
        except:
            self.log.info("Cannot click on Element with locator: " + label + " and locator Type: ")
            print_stack()

    def clickUsingLabelTextInDialog(self, label):
        try:
            actions = ActionChains(self.driver)
            element = self.getDialogLabelElement(label)
            #elementID=self.getElementID(locator,locatorType)
            actions.move_to_element(element)
            actions.click(element)
            actions.perform()
            #script="document.getElementById(\""+ elementID + "\").click();"
            #self.driver.execute_script(script)
            #self.log.info(script)
            self.log.info("Clicked on Element with locator: " + label + " and locator Type: ")
        except:
            self.log.info("Cannot click on Element with locator: " + label + " and locator Type: ")
            print_stack()
