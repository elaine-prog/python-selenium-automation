from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
sleep(2)

#click account button
driver.find_element(By.ID, 'account-sign-in')

#Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//button[@type='button']").click()
sleep(7)

