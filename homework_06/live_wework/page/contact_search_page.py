# -*- coding: utf-8 -*-
# @Time   : 2021/3/6 5:31
# @Author : guoccf
# @File   : contact_search_page.py
from homework_06.live_wework.page.basepage import BasePage


class ContactSearch(BasePage):
    def get_search_result(self, search_key):
        self._params["name_value"] = search_key
        elements = self.steps("../page/contact_search_page.yaml")
        search_result_name_list = []
        for element in elements:
            search_result_name_list.append(element.text)
        return search_result_name_list
