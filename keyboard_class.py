from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com")

time.sleep(2)

# Select page content (Ctrl + A) and copy (Ctrl + C)
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# Get page text and print
content = driver.find_element(By.TAG_NAME, "body").text
print(content)

driver.quit()