# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/20 20:37
# @File    ：demo1.py
# @Function:

import requests

url = 'https://www.baidu.com/'
resp = requests.get(url)
print(type(resp))  # <class 'requests.models.Response'>
print(resp)

print()
print(type(resp.text))  # <class 'str'>
print(resp.text)  # 遇到乱码  æ´å¤äº§å

print()
print(type(resp.content))  # <class 'bytes'>  字节
print(resp.content)  # b

# 遇到乱码：先转化二进制 后解码
print()
print(resp.content.decode('utf-8'))  # 解决  更多产品
