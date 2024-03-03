# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 21:40
# @File    ：demo7WangYi.py
# @Function:

import requests
from bs4 import BeautifulSoup

resp = requests.get(
    url="https://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Referer": "https://music.163.com/"
    }
)

soup = BeautifulSoup(resp.text, features="html.parser")
parent_tag = soup.find(name='ul', attrs={"id": "m-pl-container"})

for child in parent_tag.find_all(recursive=False):
    title = child.find(name="a", attrs={"class": "tit f-thide s-fc0"}).text
    image_url = child.find(name='img').attrs['src']
    print(title, image_url)

    # 每个封面下载下来
    img_res = requests.get(url=image_url)
    file_name = title.split()[0]
    with open(f"{file_name}.jpg", mode='wb') as f:
        f.write(img_res.content)
