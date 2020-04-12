
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                # 使用已经存在的chrome进程
                #  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                # index页面会使用这个
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
        else:
            # Login与Register等页面需要用这个方法
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def finds(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by, locator)

    def switch_window(self):
        a=self._driver.current_window_handle
        self._driver.switch_to.window(a)

    def switch_alert(self):
        self._driver.switch_to_alert()

    def gundongtiao(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self._driver.execute_script(js)


    def close(self):
        sleep(20)
        self._driver.quit()
