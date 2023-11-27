# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/10 12:39
# @File    ：crawl_google.py
# @Function:

from selenium import webdriver
import os
import time
import requests
from selenium.webdriver.common.by import By


class Crawler_google_images:
    # Initialize with keyword
    def __init__(self, keyword):
        base_url = 'https://www.google.com.hk/search?q={}&tbm=isch'
        self.url = base_url.format(keyword.replace(' ', '+'))
        self.keyword = keyword

    # Initialize the browser and visit the URL
    def init_browser(self):
        browser = webdriver.Chrome()
        browser.get(self.url)
        browser.maximize_window()
        return browser

    # Download images
    def download_images(self, browser, round=2):
        picpath = '/photo/{}/'.format(self.keyword)
        if not os.path.exists(picpath):
            os.makedirs(picpath)
        count = 0
        pos = 0
        for i in range(round):
            img_url_dic = []
            pos += 500
            js = 'var q=document.documentElement.scrollTop=' + str(pos)
            browser.execute_script(js)
            time.sleep(3)
            img_elements = browser.find_elements(by=By.TAG_NAME, value='img')
            for img_element in img_elements:
                try:
                    img_url = img_element.get_attribute('src')
                    if isinstance(img_url, str) and len(img_url) <= 200 and 'images' in img_url:
                        if img_url not in img_url_dic:
                            try:
                                img_url_dic.append(img_url)
                                filename = picpath + str(count) + ".jpg"
                                r = requests.get(img_url)
                                with open(filename, 'wb') as f:
                                    f.write(r.content)
                                count += 1
                                print('this is ' + str(count) + 'st img')
                                time.sleep(0.5)
                            except:
                                print('failure')
                except Exception as e:
                    print('An error occurred:', e)

    # Run the crawler
    def run(self):
        browser = self.init_browser()
        self.download_images(browser, 6)
        browser.close()
        print("爬取完成")


# Example usage:
if __name__ == '__main__':
    # Instantiate with a keyword
    # list_keyword = ['平板', 'u盘', '沐浴露', '洗发水', '手环', '手机', '枕头', '被褥', '床单', '锅铲', '电饭煲',
    #                 '平底锅', '卡牌', '扑克牌', '旧衣服', '衣服']
    # for i in range(len(list_keyword)):
    #     craw = Crawler_google_images(list_keyword[i])
    #     craw.run()

    keyword = ''
    craw = Crawler_google_images(keyword)
    craw.run()
