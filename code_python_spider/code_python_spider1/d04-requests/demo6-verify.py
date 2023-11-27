# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 16:49
# @File    ：demo6-verify.py
# @Function: verify 证书验证


import requests

url = 'https://www.baidu.com/'
resp = requests.get(url=url, verify=False)  # 关闭证书验证
print(resp.text)  # 警告
