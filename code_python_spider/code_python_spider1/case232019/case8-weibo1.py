# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/29 17:00
# @File    ：case8-weibo1.py
# @Function:

import requests
from faker import Faker
from concurrent.futures import ThreadPoolExecutor

fake = Faker(locale='zh_CN')


def page_download(page):
    url = "https://m.weibo.cn/api/container/getIndex?"
    ua = fake.user_agent()
    headers = {
        "User-Agent": ua
    }
    param = {
        "jumpfrom": "weibocom",
        "uid": uid,
        "t": "0",
        "containerid": containerid,
        "page": page
    }
    resp = requests.get(url, headers=headers, params=param).json()
    resp_list = resp.get("data").get("cards")
    for i in range(len(resp_list)):
        src_list = resp_list[i].get("mblog").get("pics")
        if src_list is not None:
            with ThreadPoolExecutor(n2) as t2:
                for j in src_list:
                    t2.submit(img_download, j)
    print(str(page) + "页，下载完毕")


def img_download(url):
    ua = fake.user_agent()
    headers = {
        "User-Agent": ua
    }
    src = url.get("pid")
    img = "https://tva1.sinaimg.cn/large/" + src + ".jpg"
    img_resp = requests.get(img, headers=headers)
    with open(fileName + "/" + src + ".jpg", mode="wb") as f:
        f.write(img_resp.content)
    print("Finish!", src)


if __name__ == '__main__':
    # 开始页数
    page1 = 1
    # 结束页数
    page2 = 10
    # 用户id
    uid = "1642351362"
    containerid = "1076031642351362"
    # 文件名
    fileName = "杨颖"
    # 线程数
    n1 = 2
    n2 = 4

    with ThreadPoolExecutor(n1) as t1:
        for page in range(page1, page2):
            t1.submit(page_download, page)

    print(str(page1) + "到" + str(page2) + "页，全部下载完毕")
