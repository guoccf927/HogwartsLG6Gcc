# -*- coding: utf-8 -*-
# @Time   : 2021/3/14 22:00
# @Author : guoccf
# @File   : app.py
"""
启动App，跳转首页
"""
from typing import Dict

from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from homework_07.pages.basepage import BasePage
from homework_07.pages.main_page import MainPage


class App(BasePage):
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.start()
        else:
            self.driver = driver

    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空缓存启动app
        caps["noReset"] = "true"
        # 设置等待页面空闲状态的时间为0s
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待10s
        self.driver.implicitly_wait(10)
        return self

    def goto_main_page(self):
        return MainPage(self.driver)
