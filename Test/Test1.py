from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(5)
driver.maximize_window()

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("automate")
time.sleep(1)

search_box.send_keys(Keys.RETURN)

time.sleep(10)




#driver.find_element("q").send_keys("Auto")
#driver.find_element_by_name("q").send_keys("Automation Step by step")
#driver.find_element_by_name("btnk").send_keys(Keys.ENTER)

#time.sleep(5)
