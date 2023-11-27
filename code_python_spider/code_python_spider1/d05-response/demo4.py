# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/20 21:24
# @File    ：demo4.py
# @Function:


import requests

url = 'https://dict.youdao.com/keyword/key'
data = {
    "xt": "how old are you"
}
resp = requests.post(url=url, data=data)
print(resp.text)  # {"code":0,"message":"SUCCESS","data":[]}
print(resp.json()['message'])

import json  # 内置

data_json = json.loads(resp.text)  # 字符串转成json
print(type(data_json))  # {'code': 0, 'message': 'SUCCESS', 'data': []}
data_str = json.dumps(data_json)  # json转化为字符串
print(type(data_str))