from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")
sleep(2)
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Selenium (software)")
driver.find_element(By.CSS_SELECTOR, "button.pure-button").click()
sleep(2)

print("Navigating to Selenium (software): ", driver.title)
driver.back()  # Navigate back to the previous page
sleep(2)
print("Back to Wikipedia page: ", driver.title)
driver.forward()  # Navigate forward to the Selenium page
sleep(2)
print("Forward to Selenium (software): ", driver.title)
driver.refresh()  # Refresh the current page
sleep(2)
print("Page refreshed: ", driver.title)
driver.quit()
