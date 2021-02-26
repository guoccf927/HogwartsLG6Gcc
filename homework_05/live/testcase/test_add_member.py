# -*- coding: utf-8 -*-
# @Time   : 2021/2/26 23:51
# @Author : guoccf
# @File   : test_add_member.py
import datetime
import random

from homework_05.live.page.main_page import MainPage


class TestMember:
    def setup(self):
        """
        准备工作：
        1、打开企业微信首页
        2、扫码登录
        3、停留在首页页签下
        代码解析：
        1、实例化一个对象
        2、MainPage() 继承 BasePage
        3、首先执行 BasePage 的__init__函数
        4、首页登录成功
        :return: self.driver
        """
        self.main_page = MainPage()

    def test_add_member(self):
        """
        1、进入 添加成员 页面
        2、输入 用户信息，点击保存（兼容翻页）
        3、进入 通信录 页面
        4、校验 用户名、手机号
        """
        # 获取随机数
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        number = random.randint(11111111, 99999999)

        # 用户信息
        username = f"name_{now_time}"
        account = f"account_{now_time}"
        phone = f"132{number}"

        # 进入 通讯录 获取列表信息
        info_list = self.main_page.goto_add_member().add_member(username, account, phone).get_user_info()

        # 用户名 正确
        assert username in info_list

        # 手机号 正确
        assert phone in info_list

    def teardown(self):
        """
        最后回到首页
        """
        self.main_page.goto_menu_index()
