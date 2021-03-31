# -*- coding: utf-8 -*-
# @Time   : 2021/3/20 18:03
# @Author : guoccf
# @File   : teacher.py.py
"""Send a reply from the proxy without sending any data to the remote server."""
import json
import sys

from mitmproxy import http

from mitmproxy import ctx
from mitmproxy.tools.cmdline import mitmdump


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)
        # 判断是否是想要的请求信息，通过url进行判断

    def response(self, flow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" \
                in flow.request.pretty_url:
            # 修改原始数据
            # 获取的text 是str类型，如果要对数据进行操作，需要进行数据转换
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["name"] = "hogwarts"
            data["data"]["items"][1]["quote"]["name"] = "hogwarts"
            data["data"]["items"][2]["quote"]["name"] = "hogwarts"
            flow.response.text = json.dumps(data)
            # 赋值给响应信息
            # 打开文件，读取文件数据，作为响应，给返回
            data = json.loads(flow.response.text)
            flow.response.text = json.dumps(self.json_travel(data))

    def json_travel(self, data):
        # 判断传入的数据类型{"a": {"b":{"c":1}}}
        if isinstance(data, dict):
            # 遍历字典的数据
            # 当字典格式，递归value值
            for key, value in data.items():
                data[key] = self.json_travel(value)
        elif isinstance(data, list):
            # 当数据类型 为 list 的时候， 添加到结构内，并继续递归遍历，
            # 知道数据类型不为可迭代对象时
            data = [self.json_travel(value) for value in data]
        elif isinstance(data, bool):
            data = data
        elif isinstance(data, int) or isinstance(data, float):
            data = data * 2
        elif isinstance(data, str):
            data = data
        else:
            data = data
        return data


addons = [
    Counter()
]

if __name__ == '__main__':
    sys.argv = [__file__, "-s", __file__]
    #
    # 官方要求必须主线程
    mitmdump()
