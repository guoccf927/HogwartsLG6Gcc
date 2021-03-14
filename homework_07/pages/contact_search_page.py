# -*- coding: utf-8 -*-
# @Time   : 2021/3/14 22:57
# @Author : guoccf
# @File   : contact_search_page.py
from homework_07.pages.basepage import BasePage
from homework_07.pages.contact_user_page import UserPage


class ContactSearchPage(BasePage):
    def search_user(self, key):
        # 输入 搜索关键字
        self._params["key"] = key
        self.parse_action("../pages/yamls/contact_search_page.yaml", "search_user")
        return self

    def verify_user_noexists(self):
        """
        校验人员不存在，不考虑重名情况
        ps: 如果要考虑搜索结果存在，但不是目标用户的话，涉及页面滚动
        :param username:
        :return:
        """
        # 校验 无搜索结果
        self.parse_action("../pages/yamls/contact_search_page.yaml", "verify_user_noexists")

    def goto_user_page(self, username):
        self._params["username"] = username
        self.parse_action("../pages/yamls/contact_search_page.yaml", "goto_user_page")
        return UserPage(self.driver)
