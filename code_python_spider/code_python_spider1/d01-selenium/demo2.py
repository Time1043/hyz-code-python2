# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/17 8:53
# @File    ：demo2.py
# @Function:

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)  # 全局策略 最大等待10s
wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID, 'kw').send_keys('通讯\n')

# 等待响应后
element = wd.find_element(By.ID, '1')
print(element.text)
