# -*- coding: utf-8 -*-
# @Time   : 2021/2/26 22:20
# @Author : guoccf
# @File   : base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    # 初始化登录
    def __init__(self, driver: WebDriver = None):
        base_url = ""
        if driver is None:
            # 由于二维码问题，使用复用浏览器方式登录
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            # 隐式等待5s
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        # 访问网页
        if base_url != "":
            self.driver.get(base_url)

    # 常用定位方法进行封装
    # 查找单个元素
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 查找批量元素
    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    # 点击按钮
    def click(self, by, locator):
        return self.find(by, locator).click()

    # 输入框输入内容
    def sen_keys(self, by, locator, content):
        return self.find(by, locator).send_keys(content)
