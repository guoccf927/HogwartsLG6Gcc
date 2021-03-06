# -*- coding: utf-8 -*-
# @Time   : 2021/3/6 1:52
# @Author : guoccf
# @File   : add_member_page.py
import time

from appium.webdriver.common.mobileby import MobileBy

from homework_06.live_wework.page.basepage import BasePage


class AddMember(BasePage):
    """
    添加成员页
    1、点击 手动输入添加
    2、跳转 手动输入添加 页面
    """

    def manual_add_single(self, user_name, user_phone):
        """
        1、输入 姓名
        2、输入 手机号
        3、点击 保存
        :return:添加成员 页面
        """

        self._params["name_value"] = user_name
        self._params["phone_value"] = user_phone
        self.steps("../page/add_member_page.yaml")
        toast_text = self._driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return toast_text
