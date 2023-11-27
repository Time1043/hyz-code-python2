# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 17:59
# @File    ：case6-tx.py
# @Function:

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://careers.tencent.com/jobopportunity.html'

wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get(url=url)

categories = wd.find_elements(By.CSS_SELECTOR, 'div[class="g-clr job-padding"]')
for category in categories:
    print(category.text)
    category.click()

    for i in range(10):
        module_job = category.find_element(By.CSS_SELECTOR, 'div[class="recruit-wrap recruit-margin"]')

        num = i
        timestamp = int(time.time())  # 获取当前时间戳
        url_template = f'''
        https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={timestamp}&
        countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006
        &parentCategoryId=&attrId=1&keyword=&pageIndex={num}&pageSize=10&language=zh-cn&area=cn
        '''



def get_category():
    pass
