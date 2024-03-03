# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 14:55
# @File    ：demo3.py
# @Function: user_agent


import requests

params = {'key': 'value'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
response = requests.get(url='https://httpbin.org/get', params=params, headers=headers)
print(response.text)  # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
