# -*- coding: utf-8 -*-
# @Time   : 2021/3/15 0:16
# @Author : guoccf
# @File   : contact_user_modify_page.py
from homework_07.pages.basepage import BasePage


class UserModifyPage(BasePage):
    def delete_user(self):
        # 点击 删除成员 按钮
        # 出现弹出框，点击 确定
        # 出现 处理中 弹出框，完毕后没有任何提示信息
        # 校验：在搜索结果页，提示 无搜索结果
        self.parse_action("../pages/yamls/contact_user_modify_page.yaml", "delete_user")
