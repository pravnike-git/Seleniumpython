from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options








driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
# point to a Chrome profile folder you used manually to pass CF



driver.get("https://admin-demo.nopcommerce.com/admin/")
time.sleep(5)
driver.maximize_window()

Email_box = driver.find_element(By.NAME, "Email")
Email_box.send_keys(Keys.CONTROL + "a")
Email_box.send_keys(Keys.DELETE)
time.sleep(5)
Email_box.send_keys("admin@yourstore.com")

Password_box = driver.find_element(By.NAME, "Password")
Password_box.send_keys(Keys.CONTROL + "a")
Password_box.send_keys(Keys.DELETE)
time.sleep(5)
Password_box.send_keys("admin")


Password_box.send_keys(Keys.ENTER)

time.sleep(100)
