from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)

actions = ActionChains(driver)

# Locate sliders (they are the first and second handles)
min_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")

# ---- Adjust Min Slider to $200 ----
actions.click_and_hold(min_slider).move_by_offset(-30, 0).release().perform()
time.sleep(1)

# ---- Adjust Max Slider to $250 ----
actions.click_and_hold(max_slider).move_by_offset(-10, 0).release().perform()
time.sleep(100)