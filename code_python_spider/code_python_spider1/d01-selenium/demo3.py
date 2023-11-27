# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/18 15:19
# @File    ：demo3.py
# @Function:

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/test3.html')

element = wd.find_element(By.ID, 'input1')
element.send_keys('周坚深')

print(element.get_attribute('outerHTML'))  # 全部HTML
print(element.get_attribute('innerHTML'))  # 内部HTML
print(element.get_attribute('value'))  # 获取输入框文字

sleep(5)
element.clear()
element.send_keys('周坚深')

sleep(5)
wd.quit()
