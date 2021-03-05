# -*- coding: utf-8 -*-
# @Time   : 2021/2/25 17:57
# @Author : guoccf
# @File   : testwechat.py
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"


class TestWeChat:

    def setup(self):

        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_address(self):

        # 将带有登录信息的cookie加入当前页面
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'v0hjJ_TFUaQzhYz4nTT0SOMSVknKfto9sBsA8yzoxYUSNglFTj45nCay569LL_vPemyCz8OXKR6ZqAVfGZS6K0OAhpnLs4IeK78JCY_PgmpmA8gXCH2umLq56z8UjtNhkeGlEwgmgnYUsc8MZsjhbVJmJ2avOflqL6LemCvMlbyG3FokKlT_TqOr0aXTJxWAatw3yK301HsbQKwAjaz-ggCdIJoqRkZ4SJ4i9m-dDuAQ80mL5nVU9RmbSZ3ppMhR9IPAsio03suoGkf-x3bPhA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688852028960271'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324977421399'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'Ek4tZCBv8hDm-1ZOR_AsxiTCPH5Oh5rDBfpUcrJlXQCZt0Oqhwo_3nxsXFkMmotl'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3056960'},
            {'domain': '.qq.com', 'expiry': 1614349457, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '6046797904'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1645885397, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1614239168,1614248761,1614349255,1614349397'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1614349397'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '9489517731394492'},
            {'domain': '.qq.com', 'expiry': 1614435807, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.591996458.1614349256'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1614380791, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '1ub9j4u'},
            {'domain': '.qq.com', 'expiry': 1677421407, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.857595101.1614349256'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1645668606, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1616941410, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688852028960271'},
            {'domain': '.qq.com', 'expiry': 1929426431, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False,
             'value': '0'},
            {'domain': '.qq.com', 'expiry': 1920937159, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_abad06d184996'}]

        for cookie in cookies:
            if "expiry" not in cookie.keys():
                self.driver.add_cookie(cookie)

        # excel文件路径 os.sep
        # path_list = ['E:', '97 测试文件', '自定义分类', '自定义分类.xls']
        # excel_path = ""
        # for path in path_list:
        #     if path_list.index(path) < len(path_list)-1:
        #         excel_path += path + os.sep
        #     else:
        #         excel_path += path
        excel_path = "E:/97 测试文件/自定义分类/自定义分类.xls"
        print(excel_path)

        # 刷新页面，登录成功
        self.driver.refresh()

        # 点击“导入通讯录”
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        # 点击“上传文件”
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(excel_path)

        # 断言
        excel_name = self.driver.find_element(By.ID, "upload_file_name").text
        print(excel_name)
        assert "自定义分类.xls" == excel_name

    def teardown(self):
        self.driver.quit()
