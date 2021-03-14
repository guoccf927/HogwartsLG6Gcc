# -*- coding: utf-8 -*-
# @Time   : 2021/3/15 0:14
# @Author : guoccf
# @File   : contact_user_details_page.py
from homework_07.pages.basepage import BasePage
from homework_07.pages.contact_user_modify_page import UserModifyPage


class UserDetailsPage(BasePage):
    def goto_user_modify_page(self):
        # 点击 编辑成员 按钮
        self.parse_action("../pages/yamls/contact_user_details_page.yaml", "goto_user_modify_page")
        return UserModifyPage(self.driver)
