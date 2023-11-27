# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/1 10:41
# @File    ：utils.py
# @Function:

import json

from selenium import webdriver


def create_chrome_driver(*, headless=False):
    '''创建chrome浏览器对象'''
    options = webdriver.ChromeOptions()
    if headless:  # 无头浏览器
        options.add_argument('--headless')

    # 伪装selenium
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 创建浏览器对象
    browser = webdriver.Chrome(options=options)
    # 破解selenium防爬
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
    )
    return browser


def add_cookies(browser, cookie_file):
    '''向chrome对象写入cookies'''
    with open(cookie_file, 'r') as file:
        cookie_list = json.load(file)
        for cookie_dict in cookie_list:
            if cookie_dict['secure']:
                browser.add_cookie(cookie_dict)
