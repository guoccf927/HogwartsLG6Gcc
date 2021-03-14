# -*- coding: utf-8 -*-
# @Time   : 2021/3/14 21:46
# @Author : guoccf
# @File   : main_page.py
from homework_07.pages.basepage import BasePage
from homework_07.pages.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact_page(self):
        # 点击 通讯录
        self.parse_action("../pages/yamls/main_page.yaml", "goto_contact_page")
        return ContactPage(self.driver)
