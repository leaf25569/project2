
from time import sleep

from selenium.webdriver.common.by import By

from web.Page.BasePage import BasePage


class Index(BasePage):

    def download(self):
        self.find((By.CSS_SELECTOR, '.index_explore_item_operation')).click()
        self.find((By.CSS_SELECTOR, '.qui_dialog_close ')).click()

    def invite(self):
        self.finds((By.CSS_SELECTOR, '.index_explore_item_operation'))[1].click()
        self.find((By.CSS_SELECTOR, '.ww_commonImg_CloseDialog')).click()

    def go_chakan(self):
        self.finds((By.CSS_SELECTOR, '.index_explore_item_operation'))[2].click()
        self.find((By.CSS_SELECTOR, '.ww_commonImg_CloseDialog'))

    def addmember(self):
        # 回到首页
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()
        self.find((By.CSS_SELECTOR, '.ww_indexImg_AddMember')).click()
        self.switch_window()
        self.find((By.CSS_SELECTOR, '#username')).send_keys('buye')
        self.find((By.LINK_TEXT, '保存')).click()
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()
        self.find((By.LINK_TEXT, '离开此页')).click()
        return True

    def leadconcat(self):
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()
        self.finds((By.CSS_SELECTOR, '.index_service_cnt_item_title'))[1].click()
        self.switch_window()
        # self.find((By.LINK_TEXT,'返回')).click()
        self.find((By.CSS_SELECTOR, '#js_upload_file_input')).send_keys(r'C:\Users\Administrator\Desktop\1.xls')
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()

    def memberjoin(self):
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()
        self.finds((By.CSS_SELECTOR, '.index_service_cnt_item_title'))[2].click()
        self.find((By.CSS_SELECTOR,'.ww_commonImg_SmallSwitch')).click()
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()

    def messagequnfa(self):
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()
        self.finds((By.CSS_SELECTOR, '.index_service_cnt_item_title'))[3].click()
        self.switch_window()
        self.find((By.LINK_TEXT,'选择需要发消息的应用')).click()
        sleep(2)
        self.find((By.CSS_SELECTOR,'.js_app_dlg_item')).click()
        self.find((By.LINK_TEXT,'确定')).click()
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()
        self.find((By.LINK_TEXT, '离开此页')).click()

    def kehulianxi(self,a):
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()
        self.finds((By.CSS_SELECTOR, '.index_service_cnt_item_title'))[4].click()
        self.switch_window()
        self.find((By.LINK_TEXT,'客户群')).click()
        self.find((By.CSS_SELECTOR,'.js_qunMaster_text')).click()
        self.finds((By.CSS_SELECTOR,'#memberSearchInput'))[-1].send_keys(a)
        self.find((By.LINK_TEXT,'取消')).click()
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()

    def daka(self):
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()
        self.finds((By.CSS_SELECTOR, '.index_service_cnt_item_title'))[5].click()
        self.gundongtiao()
        self.find((By.LINK_TEXT,'1年')).click()
        self.finds((By.CSS_SELECTOR, '.frame_nav_item_title'))[0].click()








