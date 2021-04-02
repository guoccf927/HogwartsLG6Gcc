# -*- coding: utf-8 -*-
# @Time   : 2021/4/1 17:22
# @Author : guoccf
# @File   : test_member.py
import datetime
import random

import pytest

from homework_09.work2_session.testcase.conf import member_info_list
from homework_09.work2_session.wework.member_management import MemberManagement


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

    @pytest.mark.parametrize("userid, mobile", [
        (member_info_list[0]["userid"], member_info_list[0]["mobile"]),
        (member_info_list[1]["userid"], member_info_list[1]["mobile"]),
        (member_info_list[2]["userid"], member_info_list[2]["mobile"]),
        (member_info_list[3]["userid"], member_info_list[3]["mobile"]),
        (member_info_list[4]["userid"], member_info_list[4]["mobile"]),
        (member_info_list[5]["userid"], member_info_list[5]["mobile"]),
        (member_info_list[6]["userid"], member_info_list[6]["mobile"]),
        (member_info_list[7]["userid"], member_info_list[7]["mobile"]),
    ])
    def test_create_member(self, userid, mobile):
        """
        安装：本地安装pytest-xdist，项目中也需要install pytest-xdist
        注意：并行用例设计不要冲突，比如以下情况：
            并行用例中存在数据相同（随机数：时间种子）
            并行用例端口相同
            并行用例本地的文件相同：进程锁
            如何自行设计并行套件，可参考 pytest 的 hook：pytest_collection_modifyitems
        """
        # 添加用户
        res = self.member.create_member(userid, self.name, mobile, self.department)
        # 删除用户
        self.member.delete_member(userid)
        # 校验返回值
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
