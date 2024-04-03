import time


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        driver.implicitly_wait(timeout)

    def open_link(self):
        self.driver.get(self.url)

    def refresh_page(self):
        time.sleep(1)
        self.driver.refresh()
