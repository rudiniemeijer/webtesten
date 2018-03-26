# All the imports we do
import unittest
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

# In order to move the stuff below in their own files,
# use from NameOfFile import *, or NameOfFile import class

# Stuff that needs to go in the configuration
settings = dict(
    driverpath = './chromedriver',
    baseurl = 'https://www.google.nl',
    maxviablewaittime = 5
)

# Stuff that needs to go in the fixtures where settings are imported
max_viable_wait_time = settings['maxviablewaittime'] # A test fails when page loading takes longer than this wait time
chrome_driver_path = settings['driverpath']
URL = settings['baseurl']

# Definition of classes of tests
class basicTests(unittest.TestCase):
    # Start the browser, go to the URL, perhaps do the login
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.get(URL)
        self.driver.maximize_window()

    # This counts as one test, even if there are numerous asserts in this test
    def testCheckTitle(self):
        self.assertTrue('Google' in self.driver.title, 'Check, Google appears in the page title')

    def testSendSearchText(self):
        try:
            element = EC.visibility_of_element_located((By.XPATH, '//*[@id="lst-ib"]'))
            WebDriverWait(self.driver, max_viable_wait_time).until(element)
        except TimeoutException:
            self.assertTrue(False, 'Page did not load in time')

        element = self.driver.find_element_by_xpath('//*[@id="lst-ib"]')
        element.clear()
        element.send_keys('Python rulez')
        element.send_keys(Keys.RETURN)

        try:
            element = EC.visibility_of_element_located((By.XPATH, '//*[@id="resultStats"]'))
            WebDriverWait(self.driver, max_viable_wait_time).until(element)
        except TimeoutException:
            self.assertTrue(False, 'Results did not show in time')

        element = self.driver.find_element_by_xpath('//*[@id="resultStats"]')
        response = element.text
        self.assertTrue('resultaten' in response, 'Not the expected response')
        responseSet = response.split(' ') # split the response at the spaces
        print(responseSet[1] + " resultaten .. ")

    # End the session here. More that one test can have run at this time
    def tearDown(self):
        self.driver.quit()

# Here the actual run-the-tests
suite = unittest.TestSuite()
suite.addTest(basicTests('testCheckTitle'))
suite.addTest(basicTests('testSendSearchText'))
runner = unittest.TextTestRunner(verbosity = 2)
result = runner.run(suite)
