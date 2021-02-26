# -*- coding: utf-8 -*-
# @Time   : 2021/2/26 22:52
# @Author : guoccf
# @File   : menu_contacts_page.py
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from homework_05.live.page.base_page import BasePage


class MenuContactsPage(BasePage):
    def get_user_info(self):
        """
        兼容分页问题
        1、直接取第一页内容
        2、当 js_next_page 翻页元素不存在时，直接pass
        3、当 js_next_page 翻页元素存在时，循环点击并取出当页内容，直到该元素属性不可点击
        :return: 通讯录的全部信息
        """
        # 获取用户信息
        info_list = []

        # 取首页内容
        ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
        for ele in ele_list:
            info_list.append(ele.get_attribute("title"))

        # 取出翻页元素的属性
        try:
            while 1:
                # 点击 下一页
                self.click(By.CSS_SELECTOR, ".js_next_page")

                # 获取当页内容
                ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
                for ele in ele_list:
                    info_list.append(ele.get_attribute("title"))

                # 输出当前页数
                print(self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text)

                # 输出 下一页 按钮的属性
                button_attribute = self.find(By.CSS_SELECTOR, ".js_next_page").get_attribute("disabled")

                # 下一页 按钮不可点击,即该按钮的disabled属性为true时，跳出循环
                if button_attribute == "true":
                    break

        except NoSuchElementException as e:
            print("except:", e)

        print(info_list)
        return info_list

    def goto_add_member(self):
        # 点击 添加成员
        self.click(By.CSS_SELECTOR, ".js_add_member")
