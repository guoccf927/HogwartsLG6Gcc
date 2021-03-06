# -*- coding: utf-8 -*-
# @Time   : 2021/3/6 0:43
# @Author : guoccf
# @File   : main_page.py
from homework_06.live_wework.page.basepage import BasePage
from homework_06.live_wework.page.contact_page import ContactPage


class MainPage(BasePage):

    def goto_contact(self):
        self.steps("../page/main_page.yaml")
        return ContactPage(self._driver)
