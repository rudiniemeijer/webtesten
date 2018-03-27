from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('./chromedriver')

for i in range(25):
    driver.get("https://www.youngcapital.nl/")
    assert "YoungCapital" in driver.title

    elem = driver.find_element_by_xpath('//*[@placeholder="Plaatsnaam of postcode"]')
    elem.clear()
    elem.send_keys("Zwolle")
    knop = driver.find_element_by_xpath('//*[@id="job_opening_search"]/div/div[4]/div[1]/button')
    knop.click()

driver.close()
