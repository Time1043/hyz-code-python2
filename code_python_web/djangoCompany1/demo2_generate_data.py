# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/5 15:52
# @File    ：demo2_generate_data.py
# @Function:

import os
import random
import django
from faker import Faker
from tqdm import tqdm

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoCompany1.settings")
django.setup()
from app01.models import PrettyNum

fake = Faker('zh_CN')


def generate_pretty_num_data(unique_numbers):
    while True:
        mobile = fake.phone_number()  # 生成随机手机号码
        if mobile not in unique_numbers:  # 检查手机号码是否唯一
            break

    price = round(random.uniform(0, 10000), 2)  # 生成随机价格，这里我设定的是0到1000之间
    level_choices = [1, 2, 3]  # 随机选择一个级别
    level = random.choice(level_choices)
    status_choices = [0, 1]  # 随机选择一个状态
    status = random.choice(status_choices)

    unique_numbers.add(mobile)  # 将生成的手机号码添加到集合中，用于后续的唯一性检查

    return {
        "mobile": mobile,
        "price": price,
        "level": level,
        "status": status
    }


# 获取数据库中已经存在的手机号码
existing_numbers = set(PrettyNum.objects.values_list('mobile', flat=True))

# 创建并保存靓号数据到数据库
for _ in tqdm(range(500), desc="Generating data"):
    data = generate_pretty_num_data(existing_numbers)
    pretty_num = PrettyNum(**data)
    pretty_num.save()
