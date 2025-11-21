import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username,password",
                             [
                                 ("test","test"),
                                 ("user2","pass2"),
                                 ("user3","pass3"),
                             ])

def test_login(driver,username,password):
    driver.get("https://trytestingthis.netlify.app/")
    username_field = driver.find_element(By.ID, "uname")
    passwrod_field = driver.find_element(By.ID, "pwd")
    submit_button = driver.find_element(By.XPATH, "//input[@value='Login']")

    username_field.send_keys(username)
    passwrod_field.send_keys(password)
    time.sleep(3)
    submit_button.click()
    assert "Successful" in driver.page_source
    time.sleep(3)