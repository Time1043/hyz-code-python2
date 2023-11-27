# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/20 21:13
# @File    ：demo3.py
# @Function:


import requests

url = 'https://dict.youdao.com/webtranslate'
data = {
    "i": "你好",
    "from": "auto",
    "to": "",
    "domain": "0",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": "b1c1c9e1d287923dc35b1e9a397932b6",
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": "1697807414662",
    "keyfrom": "fanyi.web",
    "mid": "1",
    "screen": "1",
    "model": "1",
    "network": "wifi",
    "abtest": "0",
    "yduuid": "abcdefg"
}

resp = requests.post(url=url, data=data)
# print(resp.content.decode('utf-8'))
print(resp.json())
