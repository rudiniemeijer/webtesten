from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as wacht

driver = webdriver.Chrome('./chromedriver')

for i in range(1, 11):
    driver.get("http://www.retro-lab.nl")
    assert "Retro-Lab" in driver.title

    plaatje = driver.find_element_by_xpath('//*[@id="post-1616"]/a/img')
    plaatje.click()

    # Reactie achterlaten
    reactieveld = driver.find_element_by_id('comment')
    reactieveld.send_keys('Hallo vrienden, wat een stom artikel. Blrrrrr.')
    auteurveld = driver.find_element_by_id('author')
    reactieveld.send_keys('Grote Smurf')
    emailveld = driver.find_element_by_id('email')
    emailveld.send_keys('grotesmurf@itph-academy.nl')
    submitknop = driver.find_element_by_id('submit')
    wacht(2)


driver.close()
