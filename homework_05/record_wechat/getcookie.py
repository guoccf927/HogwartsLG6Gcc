# -*- coding: utf-8 -*-
# @Time   : 2021/2/25 18:01
# @Author : guoccf
# @File   : getcookie.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestCookie:

    def test_cookie(self):

        # 复用浏览器
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)

        # 获取登录状态下的cookie
        cookies = self.driver.get_cookies()
        print(cookies)
