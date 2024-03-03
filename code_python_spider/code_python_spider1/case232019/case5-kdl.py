# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 15:56
# @File    ：case5-kdl.py
# @Function:

from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

num = 1
url = f'https://www.kuaidaili.com/free/inha/1/'

# for i in range(num):
resp = requests.get(url)
print(resp.text)






