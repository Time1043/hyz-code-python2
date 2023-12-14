# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/13 18:13
# @File    ：demo3HuaBan.py
# @Function: 花瓣网  发送请求

import requests
import json

url = 'https://api.huaban.com/search/file?text=%E7%BE%8E%E5%A5%B3&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN,total,facets,split_words,relations,recommend_topics'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

resp = requests.get(url=url)

# 图片地址列表
img_list = []
img_url_list = []
str1 = 'https://gd-hbimg.huaban.com/'
str2 = '_fw240webp'

# print(resp.text)  # 字符串
data_dict = json.loads(resp.text)
pin_list = data_dict['pins']
for item in pin_list:
    img_list.append(item['file']['key'])
    img_url_list = [str1 + element + str2 for element in img_list]
print(img_url_list)
