# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 21:30
# @File    ：demo6YiChe.py
# @Function:

import requests
from bs4 import BeautifulSoup

resp = requests.get(url='https://car.yiche.com/')
soup = BeautifulSoup(resp.text, features='html.parser')
tag_list = soup.find_all(name='div', attrs={'class': 'item-brand'})
# 分析1
for tag in tag_list:
    print(tag.attrs['data-name'])
# 分析2
for tag in tag_list:
    child = tag.find(name='div', attrs={'class': 'brand-name'})
    print(child.text)
