# -*- coding: utf-8 -*-
# @Time   : 2021/4/2 14:35
# @Author : guoccf
# @File   : base.py
import requests

from homework_09.work2_session.wework.member_conf import TestConf


class Base:
    def __init__(self):
        self.session = requests.session()
        self.access_token = self.get_token()
        self.session.params = {"access_token": self.access_token}

    def get_token(self):
        # corpid:企业ID, corpsecret:应用的凭证密钥
        corpid = TestConf["CORP_ID"]
        corpsecret = TestConf["CONTACT_SYNC_SECRET"]
        get_token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(get_token_url)
        access_token = r.json()["access_token"]
        print(f"get_token响应结果\n {access_token}")
        return access_token

    def send(self, *args, **kwargs):
        return self.session.request(*args, **kwargs)
