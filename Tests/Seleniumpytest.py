import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_practice(driver):

    driver.get("https://practicetestautomation.com/practice-test-login/")

    time.sleep(5)
    driver.maximize_window()

    print("Test Completed")