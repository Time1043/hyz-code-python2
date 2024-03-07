# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/3/3 17:04
# @File    ：demo21_re.py
# @Function:

import functools
import re

import requests


def write_to_csv(func):
    def wrapper(*args, **kwargs):
        with open('top250.csv', mode='a', encoding='utf-8') as file:
            func(file=file, *args, **kwargs)  # 将文件对象作为参数传递给func

    return wrapper


def req_douban25(page):  # 额外接受一个参数file
    url = f'https://movie.douban.com/top250?start={(page - 1) * 25}&filter='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'

    pattern = re.compile(r'<div class="item">.*?<span class="title">(?P<title>.*?)</span>.*?'
                         r'<p class="">.*?导演: (?P<director>.*?)&nbsp;.*?<br>(?P<year>.*?)&nbsp;.*?'
                         r'<span class="rating_num" property="v:average">(?P<rate>.*?)</span>.*?'
                         r'<span>(?P<comment>.*?)人评价</span>', re.S)  # re.S 让正则的.匹配换行符

    for item in pattern.finditer(resp.text):
        yield {
            'title': item.group('title'),
            'director': item.group('director'),
            'year': item.group('year').strip(),
            'rate': item.group('rate'),
            'comment': item.group('comment'),
        }


@write_to_csv
def process(file):
    for page in range(1, 11):
        for data in req_douban25(page):
            print(data)  # 验证成功
            file.write(f"{data['title']},{data['director']},{data['year']},{data['rate']},{data['comment']}\n")


if __name__ == '__main__':
    print('start...')

    # req_douban25()
    process()

    print('end...')
