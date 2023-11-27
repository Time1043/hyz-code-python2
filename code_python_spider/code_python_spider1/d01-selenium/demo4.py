# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/18 16:00
# @File    ：demo4.py
# @Function: CSS选择器

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

element = wd.find_element(By.CSS_SELECTOR, '[id="searchtext"]')
element.send_keys('第一次输入')

elements = wd.find_elements(By.CSS_SELECTOR, 'div[class="animal"]')
for element in elements:
    print(element.text)

element = wd.find_element(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
print(element)

elements = wd.find_elements(By.CSS_SELECTOR, '[class]')
for element in elements:
    print(element.text)

sleep(5)
wd.quit()
