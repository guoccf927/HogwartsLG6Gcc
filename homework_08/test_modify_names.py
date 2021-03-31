# -*- coding: utf-8 -*-
# @Time   : 2021/3/20 19:01
# @Author : guoccf
# @File   : test_modify_names.py
"""
使用mitmproxy，贴出来脚本内容和效果截图
对第一个股票保持原样
对第二个股票名字加长一倍
对第三个股票名字变成空
"""
import json
import sys

from mitmproxy import http, ctx
from mitmproxy.tools.main import mitmdump


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)
        # 判断是否是想要的请求信息，通过url进行判断

    def response(self, flow: http.HTTPFlow):
        name_url = "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t="
        if name_url in flow.request.pretty_url:
            print("---------begin---------")
            # 修改原始数据
            data = json.loads(flow.response.text)
            data["data"]["items"][1]["quote"]["name"] = "阿里巴巴" * 2
            data["data"]["items"][2]["quote"]["name"] = ""
            # 赋值给响应信息
            flow.response.text = json.dumps(data)
        else:
            print("no exists!!!!!")


addons = [
    Counter()
]

# if __name__ == '__main__':
#
#     sys.argv = [__file__, "-s", __file__]
#
#     # 官方要求必须主线程
#     mitmdump()
