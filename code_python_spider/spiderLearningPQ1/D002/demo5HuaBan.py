# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 20:21
# @File    ：demo5HuaBan.py
# @Function: 下载图片

import requests

resp = requests.get(
    url='https://gd-hbimg.huaban.com/85655b7aa4b1c1471054af660e7c6f44ef1a26474fd6a-yoXiLP'
)

with open('v1.png', mode='wb') as f:
    f.write(resp.content)
