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

    def check_username(self, username):
        """
        1、设置默认参数 False
        2、获取首页信息，判断用户名存在，则更新参数为 True
        3、首页不存在该用户名，(1) js_next_page 翻页元素不存在时，保持默认参数 False
                           (2) js_next_page 翻页元素存在，点击翻页按钮并取出当页内容，判断用户名，存在则更新参数为 True 且跳出循环
        可以传入一个参数，在while里做判断 ，判断这个人存在 ，就return True，
        另一个判断条件是，如果翻页完成，就 return False.
        :return: 默认参数 False ，找到这个人即更新参数为 True
        """
        # 设置默认参数
        exist_flag = False

        # 获取用户信息
        info_list = []

        # 取首页内容
        ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
        for ele in ele_list:
            info_list.append(ele.get_attribute("title"))

        # 用户名存在，则更新参数为 True
        if username in info_list:
            exist_flag = True
        else:
            # 取出翻页元素的属性
            try:
                while 1:
                    # 点击 下一页
                    self.click(By.CSS_SELECTOR, ".js_next_page")

                    # 获取当页内容
                    ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
                    for ele in ele_list:
                        info_list.append(ele.get_attribute("title"))

                    # 用户名存在，则更新参数为 True
                    if username in info_list:
                        exist_flag = True

                    # 跳出循环方法二
                    """
                    1、取出当前页数
                    2、当前面数字和后面数字相同时，则跳出循环
                    """
                    page_str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
                    page_list = page_str.split("/")
                    if page_list[0] == page_list[-1]:
                        break
            except NoSuchElementException as e:
                print("except:", e)
        return exist_flag

    def check_user_phone(self, phone):
        """
        1、设置默认参数 False
        2、获取首页信息，判断手机号存在，则更新参数为 True
        3、首页不存在该用户名，(1) js_next_page 翻页元素不存在时，保持默认参数 False
                           (2) js_next_page 翻页元素存在，点击翻页按钮并取出当页内容，判断手机号，存在则更新参数为 True 且跳出循环
        可以传入一个参数，在while里做判断 ，判断这个人存在 ，就return True，
        另一个判断条件是，如果翻页完成，就 return False.
        :return: 默认参数 False ，找到这个人即更新参数为 True
        """
        # 设置默认参数
        exist_flag = False

        # 获取用户信息
        info_list = []

        # 取首页内容
        ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
        for ele in ele_list:
            info_list.append(ele.get_attribute("title"))

        # 手机号存在，则更新参数为 True
        if phone in info_list:
            exist_flag = True
        else:
            # 取出翻页元素的属性
            try:
                while 1:
                    # 点击 下一页
                    self.click(By.CSS_SELECTOR, ".js_next_page")

                    # 获取当页内容
                    ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
                    for ele in ele_list:
                        info_list.append(ele.get_attribute("title"))

                    # 手机号存在，则更新参数为 True
                    if phone in info_list:
                        exist_flag = True

                    # 跳出循环方法二
                    """
                    1、取出当前页数
                    2、当前面数字和后面数字相同时，则跳出循环
                    """
                    page_str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
                    page_list = page_str.split("/")
                    if page_list[0] == page_list[-1]:
                        break
            except NoSuchElementException as e:
                print("except:", e)
        return exist_flag

    def goto_add_member(self):

        # 点击 添加成员
        self.click(By.CSS_SELECTOR, ".js_add_member")
