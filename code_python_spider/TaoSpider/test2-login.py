# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/1 11:21
# @File    ：test2-login.py
# @Function:
import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils import create_chrome_driver

url = 'https://login.taobao.com/'
browser = create_chrome_driver()
browser.get(url)

# 隐式等待
browser.implicitly_wait(10)

# 获取页面元素 模拟用户输入和点击行为
username_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-id')
username_input.send_keys('tb888406759021')
password_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-password')
password_input.send_keys('asd123fgh')
login_button = browser.find_element(By.CSS_SELECTOR, '#login-form > div.fm-btn')
login_button.click()

# 显示等待
wait_obj = WebDriverWait(browser, 10)
wait_obj.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div.m-userinfo')))

# 获取cookie数据写入文件
time.sleep(15)
with open('taobao4.json', 'w') as file:
    json.dump(browser.get_cookies(), file)
