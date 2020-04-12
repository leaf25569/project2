from selenium.webdriver.common.by import By

from web.Page.BasePage import BasePage


class Concat(BasePage):
    _base_url='https://work.weixin.qq.com/wework_admin/frame#contacts'

    def addmember(self):
        self.find((By.LINK_TEXT,'添加成员')).click()



