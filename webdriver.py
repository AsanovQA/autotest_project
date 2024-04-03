from selenium import webdriver
from enums import Browser


class WebDriverClass:
    def __init__(self, browser: webdriver):
        if browser == Browser.CHROME:
            self.driver = webdriver.Chrome()
        elif browser == Browser.FIREFOX:
            self.driver = webdriver.Firefox()
        elif browser == Browser.EDGE:
            self.driver = webdriver.Edge()
        elif browser == Browser.SAFARI:
            self.driver = webdriver.Safari()
        else:
            raise Exception("Unsupported browser!")

    def get_driver(self):
        return self.driver

    def quit(self):
        self.driver.quit()

