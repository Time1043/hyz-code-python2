# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 12:46
# @File    ：demo4Bilibili.py
# @Function:

import requests

resp = requests.get(
    url='https://api.bilibili.com/x/member/web/account?web_location=333.33',
    headers={
        "Cookie": "",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
)
print(resp.text)
