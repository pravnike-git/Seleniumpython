from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

# Create Chrome driver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)

# Enter Name
driver.find_element(By.ID, "name").send_keys("abc")

# Enter Email
driver.find_element(By.ID, "email").send_keys("abc@aabc.com")

# Select Gender (Male)
driver.find_element(By.ID, "male").click()

# Select Country = India
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("India")

# Open Datepicker
driver.find_element(By.ID, "datepicker").click()
time.sleep(1)

# Target date
target_month = "December"
target_year = "2026"
target_day = "12"

# Loop until correct month & year appear
while True:
    month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    if month == target_month and year == target_year:
        break

    # Click next button
    driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
    time.sleep(0.5)

# Click the date (12)
driver.find_element(By.XPATH, f"//a[text()='{target_day}']").click()

time.sleep(3)


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