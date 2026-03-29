from selenium import webdriver
import time

driver = webdriver.Chrome()

# Open website
driver.get("https://www.google.com")
driver.maximize_window()

time.sleep(2)

cookies = driver.get_cookies()
print("Few Cookies:")
for i in range(1):
    print(cookies[i])


driver.add_cookie({
    'name': 'test_cookie',
    'value': '12345'
})

print("Cookie Added")

print(driver.get_cookie('test_cookie'))


driver.delete_cookie('test_cookie')
print("Specific Cookie Deleted")


driver.delete_all_cookies()
print("All Cookies Deleted")

driver.quit()