# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/3 20:54
# @File    ：demo1_generate_data.py
# @Function:

import os
import random
import string
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django231103.settings")
django.setup()
from app01.models import Department, UserInfo

fake = Faker('zh_CN')

# Create some random departments
department_names = company_departments = [
    'Executive Management (高级管理)',
    'Product Management (产品管理)',
    'Information Technology (IT) (信息技术)',
    'Compliance (合规)',
    'Quality Assurance (QA) (质量保证)',
    'Supply Chain Management (供应链管理)',
    'Procurement (采购)',
    'Human Resource Development (人力资源开发)',
    'Internal Audit (内部审计)',
    'Public Relations (PR) (公共关系)',
    'Business Development (业务开发)',
    'Risk Management (风险管理)',
    'Corporate Strategy (企业战略)',
    'Innovation (创新)',
    'Data Analytics (数据分析)',
    'Infrastructure (基础设施)',
    'Technical Support (技术支持)',
    'Environmental, Health & Safety (EHS) (环境、健康与安全)',
    'Intellectual Property (IP) (知识产权)',
    'Corporate Communications (企业通信)',
    'Project Management (项目管理)',
    'Training and Development (培训与发展)',
    'Manufacturing (制造)',
    'Digital Marketing (数字营销)',
    'E-commerce (电子商务)',
    'Content Creation (内容创作)',
    'Social Media Management (社交媒体管理)',
    'Customer Relations (客户关系)',
    'Corporate Social Responsibility (CSR) (企业社会责任)',
    'Taxation (税务)',
    'Treasury (财政部)',
    'Mergers & Acquisitions (M&A) (并购)',
    'Export and Import (出口与进口)',
    'Corporate Affairs (企业事务)',
    'IT Security (信息安全)',
    'Software Engineering (软件工程)',
    'Hardware Engineering (硬件工程)',
    'Networking (网络)',
    'Employee Relations (员工关系)',
    'Diversity and Inclusion (多元化与包容)',
    'Health Services (健康服务)',
    'Investment Relations (投资者关系)',
    'Facilities Management (设施管理)',
    'Corporate Governance (公司治理)',
    'Sustainability (可持续性)',
    'Performance Management (绩效管理)',
    'Customer Experience (客户体验)',
    'Strategic Planning (战略规划)',
    'International Business (国际业务)',
    'Brand Management (品牌管理)'
]

for dept in department_names:
    Department.objects.create(title=dept)


# def generate_random_password(length=8):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for i in range(length))


def generate_random_password(length=8):
    if length < 3:
        raise ValueError(
            "Length should be at least 3 to ensure the password contains an uppercase, a lowercase, and a number.")
    # 先确保至少有一个大写字母、一个小写字母和一个数字
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    # 填充剩下的长度
    for i in range(length - 3):  # -3 是因为我们已经添加了3个字符
        characters = string.ascii_letters + string.digits
        password.append(random.choice(characters))
    # 打乱字符的顺序以确保随机性
    random.shuffle(password)
    return ''.join(password)


# Create random UserInfo entries
for _ in range(2000):  # Creating 50 random user info entries
    user = UserInfo(
        name=fake.name(),
        password=generate_random_password(),  # You should hash this before saving
        age=fake.random_int(min=20, max=60),
        account=fake.pydecimal(left_digits=8, right_digits=2, positive=True),
        create_time=fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None),
        depart=random.choice(Department.objects.all()),
        gender=fake.random_element(elements=[0, 1])
    )
    user.save()
