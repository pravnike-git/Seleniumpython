from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)

actions = ActionChains(driver)

# Locate the "Copy Text" button
copy_button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")

# Double-click
actions.double_click(copy_button).perform()

time.sleep(100)