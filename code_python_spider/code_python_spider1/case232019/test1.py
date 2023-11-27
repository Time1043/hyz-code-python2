# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 9:59
# @File    ：test1.py
# @Function:

# def compare_strings(str1, str2):
#     # 比较长度
#     if len(str1) != len(str2):
#         return False, f"两字符串的长度不同：str1长度为 {len(str1)}，str2长度为 {len(str2)}"
#
#     # 比较每个字符
#     for index, (char1, char2) in enumerate(zip(str1, str2)):
#         if char1 != char2:
#             return False, f"第 {index + 1} 个字符不同：str1中是 '{char1}'，str2中是 '{char2}'"
#
#     return True, "两字符串完全相同"
#
#
# # 测试
# str1 = input("请输入第一个字符串：")
# str2 = input("请输入第二个字符串：")
# equal, message = compare_strings(str1, str2)
#
# if equal:
#     print(message)
# else:
#     print("两字符串不相同。")
#     print(message)


# import time
# timestamp = int(time.time()) # 获取当前时间戳
# print(int(timestamp))

import requests
import time

# num = 1
# timestamp = int(time.time())  # 获取当前时间戳
# url_template = f'''
# https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={timestamp}&
# countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006
# &parentCategoryId=&attrId=1&keyword=&pageIndex={num}&pageSize=10&language=zh-cn&area=cn
# '''
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
# cookies = '''
#
# '''
# resp = requests.get(url_template, headers=headers)
# print(resp.text)
# print(resp.status_code)


# url = '''
# https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1697709461821&
# countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006
# &parentCategoryId=&attrId=1&keyword=&pageIndex=3&pageSize=10&language=zh-cn&area=cn
# '''
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
# resp = requests.get(url, headers=headers)
# print(resp.text)
# print(resp.status_code)
#
#
# cookiejar = resp.cookies
# cookies = requests.utils.dict_from_cookiejar(cookiejar)
# print(cookiejar)
# print(cookies)


import requests

proxy = {'http': 'http://221.214.224.150:8888'}
r = requests.get('http://ip.cip.cc/', proxies=proxy)
print(r.text)
