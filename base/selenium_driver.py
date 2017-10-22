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

class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def navigateTo(self,url):
        self.driver.get(url)

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        resultMessage=resultMessage.replace(" ","")
        fileName = resultMessage + "-" + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "..\\screenshots\\"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="xpath"):
        """
              To get a single elements from page
              :param locator:
              :param locatorType:
              :return element:
              """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: "+locator+ " and locator Type: "+locatorType)
        except:
            self.log.info("Element not found with locator: "+locator+ " and locator Type: "+locatorType)
        return element

    def getElementID(self,locator, locatorType="xpath"):
        elementID = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            elementID = element.get_attribute("id")
            self.log.info("Element Found with locator: " + locator + " and locator Type: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and locator Type: " + locatorType)
        return elementID

    def getElementList(self, locator, locatorType="xpath"):
        """
        To get a list of elements

        :param locator:
        :param locatorType:
        :return list of elements:
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element Found with locator: "+locator+ " and locator Type: "+locatorType)
        except:
            self.log.info("Element not found with locator: "+locator+ " and locator Type: "+locatorType)
        return element

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False


    def isWaitedElementPresent(self, locator, locatorType="xpath",
                       timeout=5, pollFrequency=0.5):
        try:
            element = self.waitForElement(locator, locatorType,timeout)
            if element is not None:
                self.log.info("Element Found with locator: " + locator + " and locator Type: " + locatorType)
                return True
            else:
                self.log.info("Element not found with locator: " + locator + " and locator Type: " + locatorType)
                return False
        except:
            self.log.info("Element not found")
            return False
    def splitButtonClick(self, locator="", locatorType = "xpath"):
        try:
            actions = ActionChains(self.driver)
            element = self.getElement(locator,locatorType)
            elementID=self.getElementID(locator,locatorType)
            actions.move_to_element(element)
            actions.click(element)
            actions.perform()
            script="document.getElementById(\""+ elementID + "\").click();"
          #  self.driver.execute_script(script)
            self.log.info(script)
            self.log.info("Clicked on Element with locator: " + locator + " and locator Type: " + locatorType)
        except:
            self.log.info("Cannot click on Element with locator: " + locator + " and locator Type: " + locatorType)
            print_stack()

    def elementClick(self, locator="", locatorType = "xpath",element=None):
        try:
            if locator:
                element=self.getElement(locator,locatorType)
            element.click()
            self.log.info("Clicked on Element with locator: "+locator+ " and locator Type: "+locatorType)
        except:
            self.log.info("Cannot click on Element with locator: "+locator+ " and locator Type: "+locatorType)
            print_stack()

    def getText(self, locator="", locatorType="xpath", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def sendKeys(self, data, locator="", locatorType = "xpath", element=None):
        """
               Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element=self.getElement(locator,locatorType)
            element.clear()
            element.send_keys(data)
            self.log.info("Data: "+data+ " entered into the field")
        except:
            self.log.info("Cannot enter Data: " + data + " into the field")
            print_stack()

    def elementPresenceCheck(self, locator, locatorType="xpath"):
        try:
            elementList = self.getElementList(locator, locatorType)
            if len(elementList) > 0:
                self.log.info("Element Found with locator: "+locator+ " and locator Type: "+locatorType)
                return True
            else:
                self.log.info("Element not found with locator: "+locator+ " and locator Type: "+locatorType)
                return False
        except:
            self.log.info("Element not found with locator: "+locator+ " and locator Type: "+locatorType)
            return False

    def waitForElement(self, locator, locatorType="xpath",
                       timeout=5, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be Visible")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.presence_of_element_located((byType,
                                                             locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def pageScroll(self, direction="up"):
        """
        To Scroll page up & Down
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")