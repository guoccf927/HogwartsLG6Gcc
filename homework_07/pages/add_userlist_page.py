# -*- coding: utf-8 -*-
# @Time   : 2021/3/15 11:31
# @Author : guoccf
# @File   : add_userlist_page.py
from homework_07.pages.add_user_manual_age import AddUserManualPage
from homework_07.pages.basepage import BasePage


class AddUserListPage(BasePage):
    def goto_add_user_manual_page(self):
        # 点击 手动输入添加
        self.parse_action("../pages/yamls/add_userlist_page.yaml", "goto_add_user_manual_page")
        return AddUserManualPage(self.driver)
