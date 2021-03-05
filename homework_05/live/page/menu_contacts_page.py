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

                # 跳出循环方法一
                """
                1、输出 下一页 按钮的属性
                2、下一页 按钮不可点击,即该按钮的disabled属性为true时，跳出循环
                """
                button_attribute = self.find(By.CSS_SELECTOR, ".js_next_page").get_attribute("disabled")
                if button_attribute == "true":
                    break

        except NoSuchElementException as e:
            print("except:", e)

        print(info_list)
        return info_list

    def check_user_info(self, info):
        """
        1、设置默认参数 False
        2、获取首页信息，判断用户名存在，则更新参数为 True
        3、首页不存在 info，(1) js_next_page 翻页元素不存在时，保持默认参数 False
                         (2) js_next_page 翻页元素存在，点击翻页按钮并取出当页内容，判断 info，存在则更新参数为 True 且跳出循环
        :return: 默认参数 False ，找到 info 即更新参数为 True
        """
        # 设置默认参数
        exist_flag = False

        # 获取用户信息
        info_list = []

        # 取首页内容
        ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
        for ele in ele_list:
            info_list.append(ele.get_attribute("title"))
        print(info_list)

        # 存在，则更新参数为 True
        if info in info_list:
            exist_flag = True
            return exist_flag

        # 取出翻页元素的属性
        try:
            while 1:
                # 点击 下一页
                self.click(By.CSS_SELECTOR, ".js_next_page")

                # 获取当页内容
                ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
                for ele in ele_list:
                    info_list.append(ele.get_attribute("title"))

                # info 存在，则更新参数为 True
                if info in info_list:
                    exist_flag = True

                # 跳出循环方法二
                """
                1、取出当前页数
                2、当前面数字和后面数字相同时，则跳出循环
                """
                page_str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
                print(f"当前页码为：{page_str}")
                page_list = page_str.split("/")
                if page_list[0] == page_list[-1]:
                    break
        except NoSuchElementException as e:
            print("except:", e)
        return exist_flag

    def goto_add_member(self):

        # 点击 添加成员
        self.click(By.CSS_SELECTOR, ".js_add_member")

    def check_user_info_last(self, check_info_list, info_list=[]):
        """
        第六阶段12节 数据驱动 所感
        :return: 默认参数 False ，找到 check_info_list 即更新参数为 True
        """
        # 设置默认参数
        exist_flag = False

        # 获取当前页用户信息
        ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
        for ele in ele_list:
            info_list.append(ele.get_attribute("title"))
        print(f"全部用户信息为：{info_list}")

        # 存在，则更新参数为 True
        if check_info_list[0] in info_list and check_info_list[1] in info_list:
            exist_flag = True
            print(exist_flag)
            return exist_flag

        try:
            """
            1、点击下一页
            2、打印当前页数
            3、循环
            """
            self.click(By.CSS_SELECTOR, ".js_next_page")
            page_str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            print(f"当前页数：{page_str}")
            return self.check_user_info_last(check_info_list, info_list)
        except NoSuchElementException as e:
            print("except:", e)
