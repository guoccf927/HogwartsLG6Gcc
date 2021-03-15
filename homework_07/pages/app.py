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
        """
        执行用例之前，需要：
        1、打开 appium server，并启动
        2、打开 mumu模拟器
        3、电脑 连接 模拟器：adb connect 127.0.0.1:7555
        参数解释：
        "platformName": "android", // 指定平台
        "deviceName": "127.0.0.1:7555", // mumu设备名称，通过 adb devices 命令获取
        "appPackage": "com.xueqiu.android", // 目标App，通过 adb logcat|grep -i displayed 命令获取
        "appActivity": ".view.WelcomeActivityAlias", // 目标页面， 通过 adb logcat|grep -i displayed 命令获取
        "noReset": "true", // 保存默认设置
        "skipServerInstallation": "true", // 规避安装
        "unicodeKeyBoard": "true", // 中文输入必备
        "resetKeyBoard": "true" // 中文输入必备
        """
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
