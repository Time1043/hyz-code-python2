# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/20 20:37
# @File    ：demo2.py
# @Function:

import requests

url = 'https://www.baidu.com/'
resp = requests.get(url)

print(resp.text)  # 直接转换成字符串 非字节码
print(resp.content)  # 图片数据 使用此参数

print()
print(resp.status_code)  # 状态码
print(resp.headers)  # 响应头
print(resp.request.headers)  # 请求头
print(resp.cookies)  # 响应cookie
print(resp.url)  # 请求的url(没用的)
print(resp.request.url)  # 请求的url(没用的)
# print(resp.json()["headers"]["User-Agent"])  # 自动转换成 字典格式


if resp.status_code == 200:
    try:
        data = resp.json()
        user_agent = data["headers"]["User-Agent"]
        print(user_agent)
    except requests.exceptions.JSONDecodeError:
        print("JSON response is empty or invalid.")
else:
    print(f"Request failed with status code: {resp.status_code}")
