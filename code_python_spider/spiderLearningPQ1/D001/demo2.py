# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/13 18:03
# @File    ：demo2.py
# @Function: 抽屉新热榜 代码模拟发送post请求

import requests

# 发送post表单请求  登录场景
url = 'https://dig.chouti.com/login'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
# post请求的请求体
data = {
    'password': '123123',
    'jid': 'wwwhhh'
}
resp = requests.post(url=url, headers=headers, data=data)  # 得到响应
print(resp.text)  # 响应体
print(resp.headers)  # 响应头
