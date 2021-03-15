# -*- coding: utf-8 -*-
# @Time   : 2021/3/15 11:37
# @Author : guoccf
# @File   : add_user_manual_age.py
from homework_07.pages.basepage import BasePage


class AddUserManualPage(BasePage):
    def add_user_manual(self, username, userphone):
        # 姓名、手机号参数
        self._params["username"] = username
        self._params["userphone"] = userphone
        # 输入 姓名
        # 输入 手机号
        # 点击 保存
        self.parse_action("../pages/yamls/add_user_manual_page.yaml", "add_user_manual")
        return self

    def verify_adduser_ok(self):
        """
        手动添加用户，点击保存， 校验 保存成功 toast
        """
        self.parse_action("../pages/yamls/add_user_manual_page.yaml", "verify_adduser_ok")
        return self

    def backto_contact_page(self):
        """
        回到 通讯录 页面，由于不能造成页面跳转循环，不能return Page
        """
        self.parse_action("../pages/yamls/add_user_manual_page.yaml", "backto_contact_page")
