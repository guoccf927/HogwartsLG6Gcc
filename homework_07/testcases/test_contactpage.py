# -*- coding: utf-8 -*-
# @Time   : 2021/3/14 23:45
# @Author : guoccf
# @File   : test_contactpage.py
from homework_07.pages.app import App


class TestContact:
    def setup(self):
        self.app = App()

    def test_check_user(self):
        # 目标用户
        key = "name_2021"
        username = "name_20210306082030"

        # 进入 通讯录 页
        contact_handle = self.app.goto_main_page().goto_contact_page().goto_contact_search_page()
        # 删除 目标用户
        contact_handle.search_user(key).goto_user_page(
            username).goto_user_details_page().goto_user_modify_page().delete_user()
        # 校验 目标用户 不存在
        contact_handle.search_user(username).verify_user_noexists()

    def teardown(self):
        self.driver.quit()
