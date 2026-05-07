from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.wait = WebDriverWait(driver, timeout=10)

# open the url
driver.get('https://www.google.com/')

# locate search box
search = driver.find_element(By.NAME, 'q')

# enter text
search.clear()
search.send_keys('Dress')

# wait for search button and click
search_btn = (By.NAME, 'btnK')

driver.wait.until(
    EC.element_to_be_clickable(search_btn),
    message='Search button not clickable'
).click()

# verify URL contains query
driver.wait.until(
    EC.url_contains('Dress'),
    message=f"Expected query not in {driver.current_url}"
)

print('Test Passed')

driver.quit()