from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("India")
sleep(3)
print("Selected by visible text: India")

driver.quit()