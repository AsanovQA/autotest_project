import time

from webdriver import WebDriverClass
from pages.loginpage import LoginPage
from enums import Browser
import pytest

driver = WebDriverClass.get_driver(WebDriverClass(Browser.CHROME))


@pytest.fixture(scope='session', autouse=True)
def browser():
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def tests_with_auth(browser):
    link = "http://34.141.58.52:8080/#/login"
    lp = LoginPage(browser, link)
    lp.open_link()
    lp.input_login('joinkids79890@gmail.com')
    lp.input_password('1234567890')
    lp.click_submit_btn()
    yield driver

    driver.quit()

