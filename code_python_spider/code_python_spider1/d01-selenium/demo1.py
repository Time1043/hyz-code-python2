# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/17 8:13
# @File    ：demo1.py
# @Function:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

wd = webdriver.Chrome()  # 对象
wd.get('https://www.baidu.com/')  # 打开网址
input('等待回车结束程序')
