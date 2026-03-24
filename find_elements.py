from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://Wikipedia.com")
sleep(2)
# Locate element
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Henry cavil")
sleep(2)
# Click button
driver.find_element(By.CSS_SELECTOR, ".pure-button.pure-button-primary-progressive").click()
sleep(2)
print(driver.title)
driver.quit()