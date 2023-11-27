# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/1 11:21
# @File    ：test3-search.py
# @Function:

from utils import create_chrome_driver, add_cookies

url = 'https://s.taobao.com/search?_input_charset=utf-8&commend=all&ie=utf8&initiative_id=tbindexz_20170306&q=ipad&search_type=item&source=suggest&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ssid=s5-e&suggest=history_1&suggest_query=&wq='
browser = create_chrome_driver()
browser.get('http://www.taobao.com')
add_cookies(browser, 'taobao3.json')
browser.get(url)
