# -*- coding: utf-8 -*-
# @Time   : 2021/2/26 22:31
# @Author : guoccf
# @File   : main_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework_05.live.page.add_member_page import AddMemberPage
from homework_05.live.page.base_page import BasePage
from homework_05.live.page.menu_contacts_page import MenuContactsPage

BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#index"  # 企业微信首页


class MainPage(BasePage):
    base_url = BASE_URL

    # 进入 添加成员 页面
    def goto_add_member(self):
        self.click(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")

        # return 跳转页面
        return AddMemberPage(self.driver)

    # 进入 通讯录 页面
    def goto_menu_contacts(self):
        self.click(By.ID, "menu_contacts")
        return MenuContactsPage(self.driver)

    # 进入 首页 页面
    def goto_menu_index(self):
        self.click(By.ID, "menu_index")
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located)
