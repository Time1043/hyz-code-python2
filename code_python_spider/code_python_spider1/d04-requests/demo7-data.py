# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 16:54
# @File    ：demo7-data.py
# @Function: data 携带表单数据发送请求


import requests

url = 'https://httpbin.org/post'
data = {
    'X-Cache:HIT TCP_MEM_HIT dirn:12': '104457820',
    'X-Oss-Cdn-Auth': 'success',
    'X-Oss-Hash-Crc64ecma': '3023017777902112144',
    'X-Oss-Meta-File-Type': 'css',
    'X-Oss-Meta-Filename': 'c__MoreFeaturesTabPanel.22199ee8.chunk.css',
    'X-Oss-Object-Type': 'Normal',
    'X-Oss-Request-Id': '65278D7776A68630312D4BFC',
    'X-Oss-Server-Time': '22',
}

resp = requests.post(url, json=data)
print(resp.text)
