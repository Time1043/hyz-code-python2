# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/1 10:51
# @File    ：test1-nologin.py
# @Function:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils import create_chrome_driver, add_cookies

# url = 'https://s.taobao.com/search?_input_charset=utf-8&commend=all&ie=utf8&initiative_id=tbindexz_20170306&q=ipad&search_type=item&source=suggest&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ssid=s5-e&suggest=history_1&suggest_query=&wq='
# url = 'https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&s=0'
url = 'https://s.taobao.com/search?_input_charset=utf-8&initiative_id=staobaoz_20231101&q=%E7%94%B5%E8%84%91&source=suggest&suggest=0_4&suggest_query=diann&wq=diann'
browser = create_chrome_driver()
browser.get(url)
