# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 15:28
# @File    ：demo5.py
# @Function: timeout 超时时间

import requests

url = 'https://www.youtube.com/'
timeout = 5
resp = requests.get(url=url, timeout=timeout)
print(resp.text)