# -*- coding: utf-8 -*-
# @Time   : 2021/3/6 1:08
# @Author : guoccf
# @File   : contact_page.py
from homework_06.live_wework.page.add_member_page import AddMember
from homework_06.live_wework.page.basepage import BasePage
from homework_06.live_wework.page.contact_search_page import ContactSearch


class ContactPage(BasePage):
    def goto_add_member(self):
        """
        1、滑动页面直到 添加成员 按钮出现
        2、点击 添加成员 按钮，跳转页面
        :return:
        """
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                         'scrollable(true).instance(0)).'
                                                         'scrollIntoView(new UiSelector().text("添加成员").'
                                                         'instance(0));').click()
        self.steps("../page/contact_page.yaml")
        return AddMember(self._driver)

    def goto_contact_search(self, ):
        """
        1、点击 搜索
        2、跳转页面
        :return:
        """

        self.clicks("xpath", '//*[@="resource-id"=com.tencent.wework:id/igk]')
        return ContactSearch(self._driver)
