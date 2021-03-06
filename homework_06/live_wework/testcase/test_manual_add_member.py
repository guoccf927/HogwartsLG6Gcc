# -*- coding: utf-8 -*-
# @Time   : 2021/3/6 2:39
# @Author : guoccf
# @File   : test_manual_add_member.py
import datetime
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework_06.live_wework.page.main_page import MainPage


class TestAdd:
    def setup(self):
        """
        用到：
        1、po
        2、滑动页面直到看到 元素
        3、yaml 调用
        问题：
        1、一个类中存在多个方法，如何使用1个yaml文件
        2、页面跳转出现循环调用，怎么解决
        :return:
        """
        self.main = MainPage()

    def teardown(self):
        pass

    def test_manual_add_single(self):
        """
        1、添加 成员
        2、校验 成员 信息
        """

        # 获取随机数
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        number = random.randint(11111111, 99999999)

        # 用户信息
        user_name = f"name_{now_time}"
        user_phone = f"131{number}"
        toast_text = self.main.goto_contact().goto_add_member().manual_add_single(user_name, user_phone)
        assert toast_text == "添加成功"
