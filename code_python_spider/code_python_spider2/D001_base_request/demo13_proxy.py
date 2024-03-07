# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/3/3 15:55
# @File    ：demo13_proxy.py
# @Function:

import requests


def get_ip():
    url = ''
    resp = requests.get(url)
    # print(resp.text)
    for ip in resp.json()['data']['proxy_list']:
        yield ip  # 生成器


def spider():
    url = 'https://baidu.com/'

    while True:
        try:
            proxy_ip = next(gen)
            proxy = {
                'http': proxy_ip,
                'https': proxy_ip,
            }

            resp = requests.get(url=url, proxies=proxy)
            resp.encoding = 'utf-8'
            return resp.text  # 直到拿到数据

        except:
            print('代理可能失效')


def req_baidu():
    proxies = {
        'http': '183.247.152.98:53281',
        'https': '183.247.152.98:53281',
    }
    url = 'https://baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    resp = requests.get(url=url, headers=headers, proxies=proxies)
    resp.encoding = 'utf-8'
    print(resp.text)  # 验证成功


if __name__ == '__main__':
    print('start...')

    # req_baidu()

    gen = get_ip()  # 代理ip的生成器
    spider()

    print('end...')
