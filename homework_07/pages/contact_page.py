# -*- coding: utf-8 -*-
# @Time   : 2021/3/14 22:54
# @Author : guoccf
# @File   : contact_page.py
from homework_07.pages.basepage import BasePage
from homework_07.pages.contact_search_page import ContactSearchPage


class ContactPage(BasePage):
    def goto_contact_search_page(self):
        # 点击 搜索
        self.parse_action("../pages/yamls/contact_page.yaml", "goto_contact_search_page")
        return ContactSearchPage(self.driver)
