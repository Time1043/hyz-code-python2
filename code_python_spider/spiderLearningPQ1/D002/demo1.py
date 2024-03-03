# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 12:02
# @File    ：demo1.py
# @Function:

import requests
import json

resp = requests.get(
    url='https://api.huaban.com/search/file',
    params={
        'text': '美女',
        'sort': 'all',
        'limit': 40,
        'page': 1,
        'position': 'search_pin',
        'fields': 'pins:PIN,total,facets,split_words,relations,recommend_topics',
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'},
)

img_list = []
img_url_list = []
str1 = 'https://gd-hbimg.huaban.com/'
str2 = '_fw240webp'

data_dict = json.loads(resp.text)
pin_list = data_dict['pins']
for item in pin_list:
    img_list.append(item['file']['key'])
    img_url_list = [str1 + element + str2 for element in img_list]
print(img_url_list)
