# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 11:55
# @File    ：case2-bl1.py
# @Function: 简单爬取b站的专栏文章


from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


# 一页一页地爬  抓取url
def crawl_url(i):
    sleep(1)
    print(f'第{i + 1}页运行')

    module_article = wd.find_element(By.CSS_SELECTOR, 'div[class="content"]')
    div_articles = module_article.find_elements(By.CSS_SELECTOR, 'div[class="s-content"]')
    for div_article in div_articles:
        a_article = div_article.find_element(By.TAG_NAME, 'a')
        list_a_article.append(a_article.get_attribute('href'))

    print(list_a_article)
    print(f'共{len(list_a_article)}条')


# 点击下一页
def click_next():
    bar = wd.find_element(By.CSS_SELECTOR, 'ul[class="be-pager"]')
    next_p = bar.find_element(By.CSS_SELECTOR, 'li[title="下一页"][class="be-pager-next"]')
    next_p.click()
    sleep(1)
    print('结束')


# 抓取每一页url和点击下一页  最后一页只抓取不点击
def crawl_click(page_num):
    # 抓取每一页面
    for i in range(page_num):
        crawl_url(i)

        if i != page_num - 1:  # 到下一个页面
            click_next()


# 根据url去请求
def req_from_url(url):
    # 伪装请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    return requests.get(url, headers=headers).content.decode('utf-8')


# 保存数据txt
def write_txt_from_urls(list_a_article, file_path):
    for i in range(len(list_a_article)):
        html = req_from_url(list_a_article[i]) + '\n\n\n\n\n\n'

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(html)

        print(f'第{i + 1}条写完')
    print('所有数据已保存')


if __name__ == '__main__':
    # 初始化 并点击打开相关网页
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    wd.get('https://space.bilibili.com/299133172')
    list_a_article = []  # 存储url的
    zl = wd.find_element(By.CSS_SELECTOR, 'a[href="/299133172/article"][class="t"]')
    zl.click()

    page_num = 6  # 获取当前页面总数
    crawl_click(page_num)

    # 最终得到的url列表
    print(list_a_article)
    print(f'最终共{len(list_a_article)}条')

    # 将爬到的数据写入本地
    file_path = 'dm.txt'
    write_txt_from_urls(list_a_article, file_path)
