from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://wikipedia.com")

# Take screenshot and save it
driver.save_screenshot("full_page.png")  

driver.quit()