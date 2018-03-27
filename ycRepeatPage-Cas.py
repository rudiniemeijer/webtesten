from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://epic.youngcapital.nl/contact")
# time.sleep(0.5)

total = 0

for i in range(100):

    driver.get("https://epic.youngcapital.nl/contact")

    name = driver.find_element_by_xpath('//*[@id="contact_reaction_name"]')
    name.clear()
    name.send_keys('test' + str(total))

    email = driver.find_element_by_xpath('//*[@id="contact_reaction_email"]')
    email.clear()
    email.send_keys('test' + str(total) + '@test.com')

    onderwerp = driver.find_element_by_xpath('//*[@id="contact_reaction_subject"]')
    onderwerp.clear()
    onderwerp.send_keys('Test' + str(total))

    bericht = driver.find_element_by_xpath('//*[@id="contact_reaction_body"]')
    bericht.clear()
    bericht.send_keys('Lorem ipsum dolor sit amet, consectetur adipiscing elit')

    bericht.submit()

    total = total + 1
    print(total)

driver.close()
