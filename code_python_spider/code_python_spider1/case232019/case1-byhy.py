# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 11:54
# @File    ：case1-byhy.py
# @Function: django网站的练习


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get('http://127.0.0.1/mgr/sign.html')


def login():
    ele_input_username = wd.find_element(By.ID, 'username')
    ele_input_password = wd.find_element(By.ID, 'password')
    ele_bt_log = wd.find_element(By.CSS_SELECTOR, 'button[type="submit"][class="btn btn-primary btn-block btn-flat"]')

    ele_input_username.send_keys('byhy')
    ele_input_password.send_keys('88888888')

    ele_bt_log.click()


def add_custom():
    ele_bt_add_custom = wd.find_element(By.CSS_SELECTOR,
                                        'button[type="button"][class="btn btn-green btn-outlined btn-md"]')
    ele_bt_add_custom.click()

    ele_add_from = wd.find_element(By.CSS_SELECTOR, 'div[class="col-lg-8 col-md-8 col-sm-8"]')
    ele_name = ele_add_from.find_element(By.XPATH, '//div[1]/input')
    ele_tel = ele_add_from.find_element(By.XPATH, '//div[2]/input')
    ele_addr = ele_add_from.find_element(By.XPATH, '//div[3]/textarea')

    ele_name.send_keys('南京中医院')
    ele_tel.send_keys('111222333')
    ele_addr.send_keys('江苏省南京市')

    ele_bt_create = wd.find_element(By.CSS_SELECTOR, 'button[type="button"][class="btn btn-green btn-outlined btn-xs"]')
    ele_bt_create.click()


if __name__ == '__main__':
    sleep(3)
    login()

    sleep(3)
    add_custom()

    sleep(3)
    wd.quit()
