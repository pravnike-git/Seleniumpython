from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)

actions = ActionChains(driver)

# Mouse hover over "Point me"
point_me_button = driver.find_element(By.XPATH, "//button[contains(text(),'Point me')]")
actions.move_to_element(point_me_button).perform()

time.sleep(1)

# Click on Mobiles
mobiles_option = driver.find_element(By.XPATH, "//a[text()='Mobiles']")
mobiles_option.click()

time.sleep(3)
driver.quit()