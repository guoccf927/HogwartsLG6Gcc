# -*- coding: utf-8 -*-
# @Time   : 2021/3/14 23:45
# @Author : guoccf
# @File   : test_contactpage.py
import datetime
import random

from homework_07.pages.app import App


class TestContact:
    def setup(self):
        self.app = App()

    def test_check_user(self):
        """
        1、添加用户后再删除
        2、用户名称搜索结果页，当前页面存在目标用户则进入用户信息页，不存在则滑动找到目标用户
        """
        # 获取随机数
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        number = random.randint(11111111, 99999999)

        # 用户信息
        username = f"name_{now_time}"
        userphone = f"131{number}"

        # 进入 通讯录 页
        contact_handle = self.app.goto_main_page().goto_contact_page()

        # 添加用户，并校验添加成功，并且回到通讯录页面
        contact_handle.goto_add_user_page().goto_add_user_manual_page().add_user_manual(username,
                                                                                        userphone).verify_adduser_ok().backto_contact_page()

        # 删除 目标用户
        search_handle = contact_handle.goto_contact_search_page()
        search_handle.search_user(username).goto_user_page(
            username).goto_user_details_page().goto_user_modify_page().delete_user()
        # 校验 目标用户 不存在
        search_handle.search_user(username).verify_user_noexists()

    def teardown(self):
        self.app.driver.quit()
