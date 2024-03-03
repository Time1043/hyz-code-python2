# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 11:01
# @File    ：caseV2.py
# @Function:

import datetime
import pandas as pd
from item import Item

EXISTING_FILE = 'RacingFactor231030.csv'  # 读取文件的文件名
FILE_NAME = f'RacingFactor{datetime.datetime.now().strftime("%y%m%d")}.csv'  # 定制文件名
new_items_list = []
new_items_list.append(Item("pythonSpider-cqc-base：", 84))
new_items_list.append(Item("dl-torch-eat2", 14))

# 读取已有的CSV文件为DataFrame（如果需要的话）
try:
    existing_df = pd.read_csv(EXISTING_FILE)
except FileNotFoundError:
    existing_df = pd.DataFrame()

# 将新的Item对象的属性保存到DataFrame中
new_data = []
for item in new_items_list:
    new_data.append(item.get_attributes())
new_df = pd.DataFrame(new_data)  # 将新数据转换为DataFrame
updated_df = pd.concat([existing_df, new_df], ignore_index=True)  # 将新数据添加到现有的DataFrame中

updated_df.to_csv(FILE_NAME, index=False)  # 保存更新后的DataFrame为CSV文件
print(updated_df)  # 打印更新后的DataFrame
