# This template examplifies the use of Cute, the minimal Cucumber Python implementation
# All the imports we do
import unittest
import time
from cute import *

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
            
    # End the session here. More that one test can have run at this time
    def tearDown(self):
        self.driver.quit()

    # This counts as one test, even if there are numerous asserts in this test
    def testCheckTitle(self):
        Given.I_start_the_browser_and_load_a_webpage_with_URL(self, URL)
        Then.I_see_this_text_in_the_driver_title(self, 'Google')

    def testSendSearchText(self):
        Given.I_start_the_browser_and_load_a_webpage_with_URL(self, URL)
        And.I_can_see_an_element_with_this_id_on_the_page(self, 'lst-ib')
        When.I_send_to_a_text_box_with_this_id_this_text(self, 'lst-ib', 'Hello, world')
        And.I_press_the_enter_key_in_the_text_box_with_this_id(self, 'lst-ib')
        Then.I_can_see_an_element_with_this_id_on_the_page(self, 'resultStats')
        And.The_element_with_this_id_contains_this_text(self, 'resultStats', 'resultaten')

    # STEP DEFINITIONS HERE
    # NOTE THAT THESE ARE METHODS OF THIS ONE CLASS
    @step
    def I_start_the_browser_and_load_a_webpage_with_URL(self, URL):
        self.driver.get(URL)
        self.driver.maximize_window()
        
    def I_see_this_text_in_the_driver_title(self, a_text)
        self.assertIn(a_text, self.driver.title, 'Nope, ' + a_text + ' does not appear in the page title')

    def I_can_see_an_element_with_this_id_on_the_page(self, an_id)
        try:
            element = EC.visibility_of_element_located((By.XPATH, '//*[@id="' + an_id + '"]'))
            WebDriverWait(self.driver, max_viable_wait_time).until(element)
        except TimeoutException:
            self.assertTrue(False, 'Element with id ' + an_id + ' did not show in time')

    def I_send_to_a_text_box_with_this_id_this_text(self, an_id, a_text)
        element = self.driver.find_element_by_xpath('//*[@id="' + an_id + '"]')
        element.clear()
        element.send_keys(a_text)

    def I_press_the_enter_key_in_the_text_box_with_this_id(self, an_id)
        element = self.driver.find_element_by_xpath('//*[@id="' + an_id + '"]')
        element.send_keys(Keys.RETURN)
        
    def The_element_with_this_id_contains_this_text(self, an_id, a_text)
        element = self.driver.find_element_by_xpath('//*[@id="' + an_id + '"]')
        element_text = element.text
        self.assertIn(a_text, element_text, 'Element ' + an_id + ' does not contain the proper text ' + a_text)

# Here the actual run-the-tests
suite = unittest.TestSuite()
suite.addTest(basicTests('testCheckTitle'))
suite.addTest(basicTests('testSendSearchText'))
runner = unittest.TextTestRunner(verbosity = 2)
result = runner.run(suite)
