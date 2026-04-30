from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://stackoverflow.com/users/signup')
sleep(2)

#CSS Selector, class "Create your account"
driver.find_element(By. CSS_SELECTOR, '.flex--item.fs-headline1')

# CSS Selector, class "clicking sign up"
driver.find_element(By. CSS_SELECTOR, 'div.flex--item.js-terms')

#email field
driver.find_element(By.CSS_SELECTOR, '#email')

#Password field
driver.find_element(By.CSS_SELECTOR, '#password')

#Password hide icon
driver.find_element(By. CSS_SELECTOR, "[d*='M3.52']")

#Sign up button
driver.find_element(By. CSS_SELECTOR, '#submit-button')

#Sign up with Google
driver.find_element(By. CSS_SELECTOR, '.flex--item.s-btn')

#Sign up with GitHub
driver.find_element(By. CSS_SELECTOR, "[data-provider='github']")

#Get stack overflow for teams link
driver.find_element(By. CSS_SELECTOR, "[target='_blank']")





