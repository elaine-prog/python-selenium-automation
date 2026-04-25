from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.target.com/")
sleep(2)

driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(7)

