# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 15:31
# @File    ：case4-ytb1.py
# @Function:

from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--proxy-server=http://202.20.16.82:10152") # 设置代理

url = 'https://www.youtube.com/'
wd = webdriver.Chrome(options=chromeOptions)

wd.get("http://httpbin.org/ip")
print(wd.page_source)




