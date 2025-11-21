from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)

actions = ActionChains(driver)

# Locate draggable and droppable elements
drag_element = driver.find_element(By.ID, "draggable")
drop_element = driver.find_element(By.ID, "droppable")

# Perform drag and drop
actions.drag_and_drop(drag_element, drop_element).perform()

time.sleep(100)