# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 20:46
# @File    ：demo7.py
# @Function: 抓取普通文本信息

import requests

res = requests.get(
    url="https://www.5xclass.cn?age=19&name=wupeiqi"
)
print(res.text)
