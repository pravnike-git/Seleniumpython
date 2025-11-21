from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(5)
driver.maximize_window()

Email_box = driver.find_element(By.NAME, "username")
Email_box.send_keys(Keys.CONTROL + "a")
Email_box.send_keys(Keys.DELETE)
time.sleep(5)
Email_box.send_keys("student")
time.sleep(5)
Email_box.send_keys(Keys.ENTER)
time.sleep(5)

Password_box = driver.find_element(By.NAME, "password")
Password_box.send_keys(Keys.CONTROL + "a")
Password_box.send_keys(Keys.DELETE)
time.sleep(5)
Password_box.send_keys("Password123")
time.sleep(5)



Submit_box = driver.find_element(By.ID, "submit")
Submit_box.click()

time.sleep(10)

expected_url_fragment = "practicetestautomation.com/logged-in-successfully/"

try:
    # Wait for the URL to contain the expected fragment within 10 seconds
    WebDriverWait(driver, 10).until(EC.url_contains(expected_url_fragment))

    # Get the current URL after the wait condition is met
    actual_url = driver.current_url

    # Assert that the expected fragment is a substring of the actual URL
    assert expected_url_fragment in actual_url, f"URL Mismatch: Expected to find '{expected_url_fragment}' in '{actual_url}'"
    print(f"Assertion Passed: URL contains '{expected_url_fragment}'")

except TimeoutError:
    # If the wait times out, capture the actual URL and fail the assertion with a custom message
    actual_url = driver.current_url
    assert False, f"Timeout or URL Mismatch: Expected to find '{expected_url_fragment}' in '{actual_url}' within 10 seconds"

finally:
    # --- Teardown ---
    driver.quit()

Logout_Button = driver.find_element(By.XPATH, "//a[contains(@class, 'wp-block-button__link') and text()='Log out']")
Logout_Button.click()
time.sleep(10)