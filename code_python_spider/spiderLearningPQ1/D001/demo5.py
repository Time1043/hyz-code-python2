# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 11:48
# @File    ：demo5.py
# @Function: 腾讯课堂

import requests

url = 'https://ke.qq.com/cgi-proxy/course_list/search_course_list?bkn=&r=0.2803'
json_str = """
{
  "mt": "1001",
  "st": "2056",
  "page": "2",
  "visitor_id": "2386988172932778",
  "finger_id": "b4041f8773ce1f8b781a74175278b77f",
  "platform": 3,
  "source": "search",
  "count": 24,
  "need_filter_contact_labels": 1
}
"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://ke.qq.com/course/list?mt=1001&quicklink=1&st=2056&page=2'}
resp = requests.post(url=url, json=json_str, headers=headers)
print(resp.text)
