# -*- coding: utf-8 -*-
# @Time   : 2021/3/31 14:50
# @Author : guoccf
# @File   : member_management.py

import requests
from homework_09.wework.member_conf import *

class MemberManagement:
    def __init__(self):
        self.access_token = self.get_token()

    def get_token(self):
        # corpid:企业ID, corpsecret:应用的凭证密钥
        corpid = TestConf["CORP_ID"]
        corpsecret = TestConf["CONTACT_SYNC_SECRET"]
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(get_token_url)
        access_token = r.json()["access_token"]
        print(f"get_token响应结果\n {access_token}")
        return access_token

    def create_member(self, userid, name, mobile, department):
        create_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(url=create_member_url, json=data)
        print(f"create_member响应结果\n {r.json()}")
        return r.json()

    def get_member_info(self, userid):
        # get 请求URL过长时，可将参数单独拎出来
        get_member_info_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {
            "access_token": self.access_token,
            "userid": userid
        }
        r = requests.get(url=get_member_info_url, params=params)
        print(f"get_member_info响应结果\n {r.json()}")
        return r.json()

    def update_member(self, userid, alias):
        update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.access_token}"
        data = {
            "userid": userid,
            "alias": alias
        }
        r = requests.post(url=update_member_url, json=data)
        print(f"update_member响应结果\n {r.json()}")
        return r.json()

    def delete_member(self, userid):
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.access_token}&userid={userid}"
        r = requests.get(delete_member_url)
        print(f"delete_member响应结果\n {r.json()}")
        return r.json()
