# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 8:40
# @File    ：demo1.py
# @Function:

from faker import Faker

fake = Faker()

# 生成虚假姓名和地址
print("虚假姓名:", fake.name())
print("虚假地址:", fake.address())

print(fake.user_agent())
