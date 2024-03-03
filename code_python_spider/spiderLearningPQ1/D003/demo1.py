# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 20:57
# @File    ：demo1.py
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
tag = soup.find(name='a')
print(tag)  # 标签对象
print(tag.name)  # 标签名字 a
print(tag.text)  # 标签文本 pythonav.com
print(tag.attrs)  # 标签属性 {'href': 'www.xxx.com', 'class': ['info']}
