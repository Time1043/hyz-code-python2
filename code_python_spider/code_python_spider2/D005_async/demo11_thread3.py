# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/3/10 16:27
# @File    ：demo11_thread3.py
# @Function:

"""
多线程爬虫，爬取所有字段
json快速处理成字符串，并实现csv文件的简单保存
但不能批量地持久化数据，只能在每次加载数据后马上保存
"""

import time
from concurrent.futures import ThreadPoolExecutor

import requests

data_file = './data2/market4.csv'
data_list = []
f = open(data_file, mode='w', encoding='utf-8')
item_keys_flag = False  # 全局变量 用来记录item_keys是否执行 (只希望item_keys执行一次)


def download_xinfadi(url, page):
    """ page个任务 """
    global item_keys_flag

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'Referer': 'http://www.xinfadi.com.cn/priceDetail.html',
    }

    data = {
        'limit': '20',
        'current': page,
        'pubDateStartTime': '',
        'pubDateEndTime': '',
        'prodPcatid': '',
        'prodCatid': '',
        'prodName': '',
    }
    resp = requests.post(url=url, data=data, headers=headers)
    # print(resp.json())  # 验证成功

    # 如果 item_keys 还没有计算过，计算它并设置全局变量
    if not item_keys_flag:
        item_keys = ','.join(resp.json()['list'][0].keys())
        item_keys_flag = True
        # print(item_keys)  # 只打印一次
        f.write(item_keys + '\n')

    for item in resp.json()['list']:
        item_values = [str(value) if value is not None else "NULL" for value in item.values()]
        item_str = ','.join(item_values) + '\n'
        f.write(item_str)
        print(item_str)  # 验证成功


def req_xinfadi():
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    with ThreadPoolExecutor(20) as t:
        for page in range(1, 50):
            time.sleep(1)
            t.submit(download_xinfadi, url, page)
            time.sleep(1)
            print(f'========================== {page} over ==========================')


if __name__ == '__main__':
    print('start...')

    req_xinfadi()

    print('end...')
