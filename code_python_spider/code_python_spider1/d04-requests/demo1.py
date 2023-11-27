# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 14:41
# @File    ：demo1.py
# @Function: url


import requests

url = 'https://www.baidu.com/'
response = requests.get(url)
print(response)  # <Response [200]>
