from .basepage import BasePage
from .locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def input_login(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginLocators.login_input)).send_keys(username)

    def input_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginLocators.password_input)).send_keys(password)

    def click_submit_btn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginLocators.login_button)).submit()
