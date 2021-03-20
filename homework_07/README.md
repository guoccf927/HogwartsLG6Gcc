# 第 7 次直播课
## 打造自己的测试框架
## 作业
> 完成删除联系人框架封装，处理异常情况，添加日志收集
## 注意
 - 多个方法调用一个yaml文件
 - 日志收集未生效
```
# 步骤一：contact_page.yaml
goto_contact_search_page:
  - by: id
    locator: com.tencent.wework:id/igk
    action: find_click

goto_add_user_page:
  - by: xpath
    locator: //*[@text="添加成员"]
    text: 添加成员
    action: slide_click

# 步骤二：读yaml 文件
def parse_action(self, path, fun_name):
        """
        操作 yaml 文件
        :param path: yaml 文件路径
        :param fun_name: 调用 yaml 文件中执行方法，适用于多个方法使用同一个 yaml 文件
        """
        # 读取 yaml 文件
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]

        # json 序列化与反序列化
        # json.dumps() 序列化  python 对象转化成字符串
        # json.loads() 反序列化  python 字符串转化为python对象
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)
        for step in steps:
            if step["action"] == "find":
                self.find(step["by"], step["locator"])
            elif step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "slide_click":
                self.slide_click(step["by"], step["locator"], step["text"])
            elif step["action"] == "find_sendkeys":
                self.find_sendkeys(step["by"], step["locator"], step["value"])
            elif step["action"] == "find_clear":
                self.find_clear(step["by"], step["locator"])
            elif step["action"] == "wait_until":
                self.wait_until(step["by"], step["locator"], step["text"])

# 步骤三：调用yaml文件
class ContactPage(BasePage):
    def goto_contact_search_page(self):
        # 点击 搜索
        self.parse_action("../pages/yamls/contact_page.yaml", "goto_contact_search_page")
        return ContactSearchPage(self.driver)

    def goto_add_user_page(self):
        # 滑动点击 添加成员
        self.parse_action("../pages/yamls/contact_page.yaml", "goto_add_user_page")
        return AddUserListPage(self.driver)
```
