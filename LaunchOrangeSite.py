from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://opensource.demo.orangehrmlive.com/")
WebDriverWait(driver, 10).until(EC.title_contains("OrangeHRM"))

# Enter invalid username, password and click on submit
driver.find_element_by_id("txtUsername").send_keys("user")
driver.find_element_by_id("txtPassword").send_keys("user")
driver.find_element_by_id("btnLogin").click()
assert "Invalid credentials" in driver.page_source


# Enter username and click on
driver.refresh()
driver.find_element_by_id("txtUsername").send_keys("user")
driver.find_element_by_id("btnLogin").click()
assert "Password cannot be empty" in driver.page_source

# Enter password and click on submit
driver.refresh()
driver.find_element_by_id("txtPassword").send_keys("user")
driver.find_element_by_id("btnLogin").click()
assert "Username cannot be empty" in driver.page_source
