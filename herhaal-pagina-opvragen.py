from selenium import webdriver
from selenium.webdriver.common.keys import Keys

test_url = "https://www.youngcapital.nl/"

driver = webdriver.Chrome('./chromedriver') # like c:\\ .. \\chromedriver.exe


for i in range(25):
    print("En daar gaan we weer..")
    print("Pagina oproepen..")
    driver.get(test_url)
    print("Paginatitel controleren..")
    assert "YoungCapital" in driver.title
    print("Invoerelement zoeken..")
    elem = driver.find_element_by_xpath('//*[@placeholder="Plaatsnaam of postcode"]')
    elem.clear()
    print("Invoerelement vullen met zoektekst..")
    elem.send_keys("Zwolle")
    knop = driver.find_element_by_xpath('//*[@id="job_opening_search"]/div/div/div[3]/div/div[2]/button')
    # //*[@id="job_opening_search"]/div/div/div[3]/div/div[2]/button
    print("Zoekknop indrukken..")
    knop.click()

    print()

driver.close()
driver.quit()
