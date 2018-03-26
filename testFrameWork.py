# All the imports we do
import unittest
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


# Stuff that needs to go in the configuration
settings = dict(
    driverpath = './chromedriver',
    baseurl = 'https://www.google.nl',
    maxviablewaittime = 60
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
    def testOne(self):
        self.assertTrue('Google' in self.driver.title, 'Check, Google appears on page')
        self.assertFalse(False, 'This one went wrong by design')
        self.assertTrue(True, 'This one went okay')

    def testTwo(self):
        print ("Short wait.. "),
        time.sleep(1)

    # End the session here. More that one test can have run at this time
    def tearDown(self):
        self.driver.quit()

# Here the actual run-the-tests
suite = unittest.TestSuite()
suite.addTest(basicTests('testOne'))
suite.addTest(basicTests('testTwo'))
runner = unittest.TextTestRunner(verbosity = 2)
result = runner.run(suite)

