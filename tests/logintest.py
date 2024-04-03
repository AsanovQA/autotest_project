import os

import pytest
from dotenv import load_dotenv
import requests
import time
from pages.loginpage import LoginPage
from core.functions import save_storage, get_auth_token
import logging

load_dotenv()
link = os.getenv('LOGIN_URL')


class TestLogin:
    @pytest.mark.regressions
    @pytest.mark.smoke
    def test_input_login(self, browser):
        browser.get(link)
        lp = LoginPage(browser, link)
        lp.input_login(os.getenv('USERNAME'))
        time.sleep(1)

    @pytest.mark.regressions
    @pytest.mark.smoke
    def test_input_password(self, browser):
        browser.get(link)
        lp = LoginPage(browser, link)
        lp.input_password(os.getenv('PASSWORD'))
        time.sleep(1)

    @pytest.mark.regressions
    @pytest.mark.smoke
    def test_submit_login_btn(self, browser):
        browser.get(link)
        lp = LoginPage(browser, link)
        lp.click_submit_btn()
        time.sleep(1)
        try:
            re = requests.get(os.getenv('PROFILE_URL'))
            if re.status_code == 200:
                is_logged_in = browser.execute_script("return localStorage.getItem('store')")
                save_storage(is_logged_in)
            else:
                logging.info(re.status_code)
        except Exception as ex:
            logging.error("We have a problem:", ex)
        assert get_auth_token() is not None

