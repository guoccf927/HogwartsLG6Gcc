# -*- coding: utf-8 -*-
# @Time   : 2021/3/15 0:03
# @Author : guoccf
# @File   : contact_user_page.py
from homework_07.pages.basepage import BasePage
from homework_07.pages.contact_user_details_page import UserDetailsPage


class UserPage(BasePage):
    def goto_user_details_page(self):
        # 点击 右上角三个点
        self.parse_action("../pages/yamls/contact_user_page.yaml", "goto_user_details_page")
        return UserDetailsPage(self.driver)
