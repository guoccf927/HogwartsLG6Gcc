# -*- coding: utf-8 -*-
# @Time   : 2021/3/6 0:16
# @Author : guoccf
# @File   : basepage.py
import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list = []
    _error_cont = 0
    _error_max = 10
    _params = {}

    def __init__(self, driver: WebDriver = None):
        _package = "com.tencent.wework"
        _activity = ".launch.WwMainActivity"
        if driver is None:
            desired_caps = {}
            desired_caps["platformName"] = "android"
            desired_caps["deviceName"] = "127.0.0.1:7555"
            desired_caps["appPackage"] = _package
            desired_caps["appActivity"] = _activity
            desired_caps["noReset"] = True
            desired_caps["autoGrantPermission"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
            self._driver.implicitly_wait(10)
        else:
            # self._driver.start_activity(_package, _activity)
            self._driver = driver

    def find(self, by, locator=None):
        """
        找元素
        :param by: 定位方式
        :param locator: 值
        :return:
        """
        try:
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                              locator)
            return element
        except Exception as e:
            # self._error_cont += 1
            # if self._error_cont >= self._error_max:
            #     raise e
            # for black in self._black_list:
            #     elements = self._driver.find_elements(*black)
            #     if len(elements) > 0:
            #         elements[0].click()
            #         return self.find()
            return e

    def send(self, value, by, locator=None):
        """
        输入框
        :param value: 输入内容
        :param by: 定位方式
        :param locator: 值
        :return:
        """
        try:
            self.find(by, locator).send_keys(value)
            self._error_cont = 0
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            return e

    def click_method(self, by, locator):
        self.find(by, locator).click()

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" in step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        content: str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}" % param, self._params[param])
                        self.send(content, step["by"], step["locator"])
