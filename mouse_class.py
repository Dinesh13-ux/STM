from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()

actions = ActionChains(driver)

element = driver.find_element(By.NAME, "q")

actions.move_to_element(element)      # Move mouse to search box
actions.click()                       # Click
actions.send_keys("Selenium Python")  # Type text
actions.double_click(element)         # Double click
actions.context_click(element)        # Right click

# Perform all actions
actions.perform()
print(driver.title)
print("Mouse actions performed successfully.")
time.sleep(5)
driver.quit()