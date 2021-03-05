# -*- coding: utf-8 -*-
# @Time   : 2021/2/26 22:32
# @Author : guoccf
# @File   : add_member_page.py
from selenium.webdriver.common.by import By
from homework_05.live.page.base_page import BasePage
from homework_05.live.page.menu_contacts_page import MenuContactsPage


class AddMemberPage(BasePage):
    def add_member(self, username, account, phone):
        # 打印用户信息
        print(f"添加用户名为：{username}")
        print(f"添加用户名账号为：{account}")
        print(f"添加用户手机号为：{phone}")

        # 输入 姓名
        self.sen_keys(By.ID, "username", username)

        # 输入 账号
        self.sen_keys(By.ID, "memberAdd_acctid", account)

        # 输入 手机号
        self.sen_keys(By.ID, "memberAdd_phone", phone)
        # 点击 保存
        self.click(By.CSS_SELECTOR, ".js_btn_save")
        return MenuContactsPage(self.driver)
