from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)

# Visitor counter is inside the stats widget (ID: stats)
visitors = driver.find_element(By.ID, "Stats1_totalCount").text

print("Total Visitors on Website:", visitors)

driver.quit()