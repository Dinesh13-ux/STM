from time import sleep
from selenium import webdriver

# 1st window
driver = webdriver.Chrome()
driver.get("https://wikipedia.com")
original_window = driver.current_window_handle
# Create a new tab
driver.switch_to.new_window('tab')
driver.get("https://google.com")
sleep(2)
print("New Tab title:", driver.title)
# Create a new window
driver.switch_to.new_window('window')
driver.get("https://youtube.com")
sleep(2)
print("New Window title:", driver.title)
# Switch back to original window
driver.switch_to.window(original_window)
print("Original window title:", driver.title)

driver.quit()