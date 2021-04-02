# -*- coding: utf-8 -*-
# @Time   : 2021/4/2 14:33
# @Author : guoccf
# @File   : member_management.py
# -*- coding: utf-8 -*-
# @Time   : 2021/3/31 14:50
# @Author : guoccf
# @File   : member_management.py
import json

from homework_09.work2_session.wework.base import Base


class MemberManagement(Base):
    def create_member(self, userid, name, mobile, department):
        create_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send("POST", create_member_url, json=data)
        print(f"create_member响应结果\n {r.json()}")
        return r.json()

    def get_member_info(self, userid):
        # get 请求URL过长时，可将参数单独拎出来
        get_member_info_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {
            "userid": userid
        }
        r = self.send("GET", get_member_info_url, params=params)
        print(f"get_member_info响应结果\n {r.json()}")
        return r.json()

    def update_member(self, userid, alias):
        update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "alias": alias
        }
        # json传参两种方式
        # r = self.send("POST", update_member_url, json=data)
        r = self.send("POST", update_member_url, data=json.dumps(data))
        # data参数如果不转换json格式，则传入的是form表单
        # r = self.send("POST", update_member_url, data=data)
        print(f"update_member响应结果\n {r.json()}")
        return r.json()

    def delete_member(self, userid):
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        r = self.send("GET", delete_member_url)
        print(f"delete_member响应结果\n {r.json()}")
        return r.json()
