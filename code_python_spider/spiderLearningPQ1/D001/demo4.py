# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 7:36
# @File    ：demo4.py
# @Function: 豆瓣

import requests
import json

# 发送get请求
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
resp = requests.get(url=url, headers=headers)  # 得到响应

movie_img_list = []
movie_title_list = []
movie_rate_list = []
movie_id_list = []

# print(resp.text)  # 字符串
data_dict = json.loads(resp.text)
data_list = data_dict['subjects']
for item in data_list:
    movie_img_list.append(item['cover'])
    movie_title_list.append(item['title'])
    movie_rate_list.append(item['rate'])
    movie_id_list.append(item['id'])
print(movie_img_list)
print(movie_title_list)
print(movie_rate_list)
print(movie_id_list)
