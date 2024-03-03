# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 15:37
# @File    ：demo5-proxies.py
# @Function: proxies 代理ip


import requests

url = 'https://httpbin.org/get'
# response = requests.get(url=url)
# print(response.text)  # "origin": "112.109.248.78"

# 设置代理ip
proxies = {
    'http': 'http://183.236.232.160:16666'
}
response = requests.get(url=url, proxies=proxies)
print(response.text)
