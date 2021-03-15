# -*- coding: utf-8 -*-
# @Time   : 2021/3/14 21:46
# @Author : guoccf
# @File   : basepage.py

import json
from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 构造的两个异常页面，返回按钮ID一致
    _blacklist = [(MobileBy.ID, "com.tencent.wework:id/ig0")]
    _error_num = 0
    _error_max = 3
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def setup_implicitly_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def find(self, by, locator):
        try:
            element = self.driver.find_element(by, locator)
            # 恢复变量的初始值，避免影响下一次调用
            self._error_num = 0
            self.setup_implicitly_wait(10)
            return element
        except Exception as e:
            # 出现异常时，将动态等待时间缩短，增加执行效率
            self.setup_implicitly_wait(2)

            # 当超过设置的循环次数上限，则返回异常
            if self._error_num > self._error_max:
                # 恢复初始值，为下一次调用做准备
                self._error_num = 0
                # 恢复初始值
                self.setup_implicitly_wait(10)
                raise e
            # 当循环次数未达到上限时，_error_num+1
            self._error_num += 1

            # 处理黑名单
            for ele in self._blacklist:
                # find_elements 会返回元素列表，如果找不到元素则返回空列表
                elements = self.driver.find_elements(*ele)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续查找目标元素，注意可能会出现死循环情况，增加循环上限避免死循环
                    return self.find(by, locator)

            # 黑名单处理完毕后仍未找到目标元素，返回异常
            raise e

    def finds(self, by, locator):
        try:
            elements = self.driver.find_elements(by, locator)
            # 恢复变量的初始值，避免影响下一次调用
            self._error_num = 0
            self.setup_implicitly_wait(10)
            return elements
        except Exception as e:
            # 出现异常时，将动态等待时间缩短，增加执行效率
            self.setup_implicitly_wait(2)

            # 当超过设置的循环次数上限，则返回异常
            if self._error_num > self._error_max:
                # 恢复初始值，为下一次调用做准备
                self._error_num = 0
                # 恢复初始值
                self.setup_implicitly_wait(10)
                raise e
            # 当循环次数未达到上限时，_error_num+1
            self._error_num += 1

            # 处理黑名单
            for ele in self._blacklist:
                # find_elements 会返回元素列表，如果找不到元素则返回空列表
                elements = self.driver.find_elements(*ele)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续查找目标元素，注意可能会出现死循环情况，增加循环上限避免死循环
                    return self.find(by, locator)

            # 黑名单处理完毕后仍未找到目标元素，返回异常
            raise e

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def slide_click(self, by, locator, text):
        """
        可直接找到元素，则直接点击
        否则，滑动页码找到 text 元素点击
        """
        # 在当前页面查看是否存在该元素
        elements = self.finds(by, locator)
        # 存在则直接点击
        if len(elements) > 0:
            elements[0].click()
        # 不存在则滑动点击
        if len(elements) == 0:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().'
                                     'scrollable(true).instance(0)).'
                                     'scrollIntoView(new UiSelector().'
                                     f'text("{text}").instance(0));').click()

    def find_sendkeys(self, by, locator, value):
        self.find(by, locator).send_keys(value)

    def find_clear(self, by, locator):
        self.find(by, locator).clear()

    def wait_until(self, by, locator, text):
        args = (by, locator)
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(args, text))

    def parse_action(self, path, fun_name):
        """
        操作 yaml 文件
        :param path: yaml 文件路径
        :param fun_name: 调用 yaml 文件中执行方法，适用于多个方法使用同一个 yaml 文件
        """
        # 读取 yaml 文件
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]

        # json 序列化与反序列化
        # json.dumps() 序列化  python 对象转化成字符串
        # json.loads() 反序列化  python 字符串转化为python对象
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)
        for step in steps:
            if step["action"] == "find":
                self.find(step["by"], step["locator"])
            elif step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "slide_click":
                self.slide_click(step["by"], step["locator"], step["text"])
            elif step["action"] == "find_sendkeys":
                self.find_sendkeys(step["by"], step["locator"], step["value"])
            elif step["action"] == "find_clear":
                self.find_clear(step["by"], step["locator"])
            elif step["action"] == "wait_until":
                self.wait_until(step["by"], step["locator"], step["text"])
