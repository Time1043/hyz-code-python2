# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 21:09
# @File    ：demo4.py
# @Function:

from bs4 import BeautifulSoup

html_string = """
<div>
    <h1 class="item">武沛齐</h1>
    <ul class="item">
        <li>篮球</li>
        <li>足球</li>
    </ul>
    <div id='x3'>
        <span>5xclass.cn</span>
        <a href="www.xxx.com" class='info'>pythonav.com</a>
        <span class='xx1'>武沛齐</span>
    </div>
</div>
"""

soup = BeautifulSoup(html_string, features='html.parser')
tag_list = soup.find_all(name='li')

print(tag_list)  # [<li>篮球</li>, <li>足球</li>]

for tag in tag_list:
    print(tag.text)  # 篮球 足球
