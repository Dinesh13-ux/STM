from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser
driver = webdriver.Chrome()

# Open website
driver.get("https://www.google.com")

print(driver.title)
sleep(10)
# Close browser
driver.quit()