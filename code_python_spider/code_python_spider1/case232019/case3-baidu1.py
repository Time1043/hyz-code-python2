# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 12:17
# @File    ：case3-baidu1.py
# @Function: 简单爬取百度热搜


from time import sleep
import requests  # 请求响应
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('https://top.baidu.com/board?tab=realtime')

# zl = wd.find_element(By.CSS_SELECTOR, 'ul[id="hotsearch-content-wrapper"]')
# print(zl.text)
# articles = zl.find_elements(By.CSS_SELECTOR,'a[class="title-content"]')
# for article in articles:
#     article.click()
#     print(article.text)

list_url = []

module_article = wd.find_element(By.CSS_SELECTOR, 'div[style="margin-bottom:20px"]')
acticles = module_article.find_elements(By.CSS_SELECTOR, 'div[class="category-wrap_iQLoo horizontal_1eKyQ"]')
for acticle in acticles[:3]:
    see_more = acticle.find_element(By.CSS_SELECTOR, 'a[class="look-more_3oNWC"][target="_blank"]')
    href = see_more.get_attribute('href')
    # print(href)
    list_url.append(href)
    # see_more.click()
    # print(acticle.text)
    # sleep(3)

print(list_url)

# 伪装请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

for url in list_url:
    print('开始')
    # print(url)
    html = requests.get(url, headers=headers).text
    print(html)
    sleep(3)
    print('结束')
