# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 20:47
# @File    ：demo8.py
# @Function: 抓取普通文本信息

import requests

res = requests.get(
    url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
)

print(res.text)
