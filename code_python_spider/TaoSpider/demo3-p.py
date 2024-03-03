# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/2 8:15
# @File    ：demo3-p.py
# @Function:
import time

import requests
from bs4 import BeautifulSoup

list_ip = []
list_prot = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
proxies = {
    "http": "http://8.219.5.240:9992",
}

for page in range(5):
    url = f'https://www.zdaye.com/dayProxy/ip/335497/{page + 1}.html'
    resp = requests.get(url=url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(resp.text, 'html.parser')

    # 获取所有的 tr 标签
    rows = soup.select('#ipc tbody tr')

    for row in rows:
        columns = row.select('td')  # 获取每个 tr 标签内的所有 td 标签
        list_ip.append(columns[0].text)  # IP地址
        list_prot.append(columns[1].text)  # 端口

    time.sleep(5)

print(resp.status_code)
print(resp.text)

print(list_ip)
print(list_prot)


# 测试
def test_proxy(list_ip, list_prot):
    url = "http://www.baidu.com/"
    # ip, port = "8.219.5.240", "9992"
    for i in list_ip:
        proxies = {"http": f"http://{list_ip[i]}:{list_prot[i]}"}
        headers = {"User-Agent": "Mozilla/5.0"}  # 响应头
        res = requests.get(url, proxies=proxies, headers=headers)  # 发起请求
        print(res.status_code)  # 返回响应码
        print(i) if res.status_code == 200 else print()
