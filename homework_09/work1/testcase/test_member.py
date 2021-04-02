# -*- coding: utf-8 -*-
# @Time   : 2021/4/1 17:22
# @Author : guoccf
# @File   : test_member.py
import datetime
import random

from homework_09.work1.wework.member_management import MemberManagement


class TestMember:
    def setup(self):
        self.member = MemberManagement()

        # 获取随机数
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        number = random.randint(11111111, 99999999)

        # 用户信息
        self.userid = f"zhangsan{now_time}"
        self.name = f"张三{now_time}"
        self.mobile = f"+86 133{number}"
        self.department = [1]

    def test_token(self):
        self.member.get_token()

    def test_create_member(self):
        res = self.member.create_member(self.userid, self.name, self.mobile, self.department)
        assert res["errmsg"] == "created"
        # 校验方式可用如下方式，避免网络原因
        # assert res.get("errmsg", "network error") == "created"

    def test_get_member_info(self):
        # 添加用户
        self.member.create_member(self.userid, self.name, self.mobile, self.department)
        # 获取用户信息
        res = self.member.get_member_info(self.userid)
        # 删除用户
        self.member.delete_member(self.userid)
        # 校验userid
        assert res["userid"] == self.userid

    def test_update_member(self):
        # 添加用户
        self.member.create_member(self.userid, self.name, self.mobile, self.department)
        # 更新昵称"alias"
        alias = f"{self.name}昵称"
        res = self.member.update_member(self.userid, alias)
        # 获取用户信息
        res_get = self.member.get_member_info(self.userid)
        # 删除用户
        self.member.delete_member(self.userid)
        # 校验返回值
        assert res["errmsg"] == "updated"
        assert res_get["alias"] == alias
