from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
sleep(2)

# By XPATH, Amazon logo
driver.find_element(By.XPATH, "//i[@role='img']")

# By ID, email
element = driver.find_element(By.ID, 'ap_email_login')
print(element)

# Continue Button,
driver.find_element(By.XPATH, '//input[@class="a-button-input"]')

# Conditions of use link
driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&amp;nodeId=508088"]')

# Privacy Notice link
driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496"]')

# Need help link
driver.find_element(By.XPATH, '//a[@class="a-size-base a-link-normal"]')

#Forgot your password link

element = driver.find_element(By.ID, 'auth-fpp-link-bottom')
print(element)

#Other issues with Sign-In link
#not present on site

#Create your Amazon account button
driver.find_element(By.XPATH, '//a[@class="a-button-input"]')

#2.Create a test case for the SignIn page using python & selenium script.
#(Make sure to use Incognito browser mode when searching for locators)







