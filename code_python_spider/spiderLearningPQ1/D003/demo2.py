# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 21:03
# @File    ：demo2.py
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
    </div>
</div>
"""

soup = BeautifulSoup(html_string, features='html.parser')
tag = soup.find(name='div', attrs={'id': 'x3'})
print(tag)
