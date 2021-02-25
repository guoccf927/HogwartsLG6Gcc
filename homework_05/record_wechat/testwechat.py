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
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852028960271'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324977421399'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Ek4tZCBv8hDm-1ZOR_AsxrbxgV7t3yZRg6S1cwlGwuQzkSANDC6Ece7yQL1fEe7_'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7372766'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '6046797904'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645784761, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614239168,1614248761'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1614248761'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '16365178551560971'}, {'domain': 'work.weixin.qq.com', 'expiry': 1614270564, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '38lm2la'}, {'domain': '.work.weixin.qq.com', 'expiry': 1645668606, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'HXLFXtYjSTzKsQsXapydT9i-KofM1SUR5WAX4MvPyQLHHGTUlCgaX5kdnVRMNid71TPBCXgEu3Q55rfjfttTkaIKD84phCSHS0E-7k-StDdMNbu3r1bK5G5-tc2rjPTnp9WoxUzme3biWi_Ds_FodrL47QfW14Eh2b85LAgseVXbV6OAANtQBvkTZh9lLos9WnbSQ3a1Gm6Q7QpW3MMlxqw6YGumBJtzVkaf_v1fElGZjJ7O57-raezFyc7eD85r87k5vpDNtzkSCQG1IPGlBg'}, {'domain': '.work.weixin.qq.com', 'expiry': 1616840777, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852028960271'}, {'domain': '.qq.com', 'expiry': 1929426431, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1920937159, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_abad06d184996'}]
        for cookie in cookies:
            if "expiry" not in cookie.keys():
                self.driver.add_cookie(cookie)

        # excel文件路径 os.sep
        path_list = ['E:', '97 测试文件', '自定义分类', '自定义分类.xls']
        excel_path = ""
        for path in path_list:
            if path_list.index(path) < len(path_list)-1:
                excel_path += path + os.sep
            else:
                excel_path += path
        # excel_path = "E:/97 测试文件/自定义分类/自定义分类.xls"
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










