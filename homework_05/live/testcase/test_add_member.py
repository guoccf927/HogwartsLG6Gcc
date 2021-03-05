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
        1、关闭 chrome 浏览器
        2、复用浏览器，Windows 命令行下执行命令：chrome --remote-debugging-port=9222
        3、在步骤2、打开的浏览器中，打开企业微信首页
        4、扫码登录
        5、停留在首页页签下
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

        # 断言方法一
        """
        思路：
        1、添加用户
        2、进入 通讯录 获取全部列表信息
        3、用户名 存在
        4、手机号 正确
        缺点：如果添加的联系人在第一页，会翻到最后一页，获取完所有的姓名再返回；如果有几十页，效率就会很低
        """
        # info_list = self.main_page.goto_add_member().add_member(username, account, phone).get_user_info()
        # assert username in info_list
        # assert phone in info_list

        # 断言方法二、
        """
        思路：
        1、添加用户
        2、进入 通讯录，获取每页信息
        3、只要 用户名 存在，则返回True
        4、只要 手机号 正确，则返回True
        """
        add_mem = self.main_page.goto_add_member().add_member(username, account, phone)
        check_username = add_mem.check_username(username)
        assert check_username
        check_user_phone = add_mem.check_user_phone(username)
        assert check_user_phone

    def teardown(self):
        """
        最后回到首页
        """
        self.main_page.goto_menu_index()
