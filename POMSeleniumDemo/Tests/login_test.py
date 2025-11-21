import pytest
from selenium import webdriver
import time
from POMSeleniumDemo.Tests.Pages.LoginPage import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.enter_username("test")
    time.sleep(1)
    login_page.enter_password("test")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)