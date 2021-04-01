# -*- coding: utf-8 -*-
# @Time   : 2021/4/1 17:22
# @Author : guoccf
# @File   : test_member.py
from homework_09.wework.member_management import MemberManagement


class TestMember:
    def setup(self):
        self.member = MemberManagement()
        self.userid = "zhangsan"
        self.name = "张三"
        self.mobile = "+86 13311110000"
        self.department = [1]

    def test_token(self):
        print(self.member.get_token())

    def test_create_member(self):
        res = self.member.create_member(self.userid, self.name, self.mobile, self.department)
        # assert res["errmsg"] == "created"
        assert res.get("errmsg", "network error") == "created"
