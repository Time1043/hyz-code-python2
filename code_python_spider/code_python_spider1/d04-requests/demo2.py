# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 14:43
# @File    ：demo2.py
# @Function: params


import requests

# response = requests.get('https://httpbin.org/get?key=value')

params = {'key': 'value'}
response = requests.get(url='https://httpbin.org/get', params=params)
print(response.text)  # "User-Agent": "python-requests/2.31.0",
