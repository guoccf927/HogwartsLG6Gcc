# 第 5 次直播课
## 企业微信 web 端自动化测试实战
## 作业
 > 完成添加联系人PO封装
## 注意
 - 每个页面都是一个单独的page
 - 添加联系人成功后，需要进行校验
 - 校验联系人时需要注意分页问题
 > 默认参数为False，找到目标用户就return True
 - 递归调用
```
ef check_user_info_last(self, check_info_list, info_list=[]):
  """
  第六阶段12节 数据驱动 所感
  :return: 默认参数 False ，找到 check_info_list 即更新参数为 True
  """
  # 设置默认参数
  exist_flag = False

  # 获取当前页用户信息
  ele_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td")
  for ele in ele_list:
      info_list.append(ele.get_attribute("title"))
  print(f"全部用户信息为：{info_list}")

  # 存在，则更新参数为 True
  if check_info_list[0] in info_list and check_info_list[1] in info_list:
      exist_flag = True
      return exist_flag

  try:
      """
      1、点击下一页
      2、打印当前页数
      3、循环
      """
      self.click(By.CSS_SELECTOR, ".js_next_page")
      page_str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
      print(f"当前页数：{page_str}")
      return self.check_user_info_last(check_info_list, info_list)
  except NoSuchElementException as e:
      print("except:", e)
```
