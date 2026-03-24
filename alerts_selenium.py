from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/alerts.html#")

sleep(2)

driver.find_element(By.ID, "alert").click()
sleep(2)
alert = driver.switch_to.alert
print(alert.text)
driver.quit()