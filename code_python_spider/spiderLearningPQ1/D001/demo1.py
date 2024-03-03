# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/13 17:56
# @File    ：demo1.py
# @Function: 豆瓣电影 代码模拟发送get请求

import requests

# 发送get请求
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

resp = requests.get(url=url, headers=headers)  # 得到响应
print(resp.text)  # 响应体
print(resp.headers)  # 响应头
