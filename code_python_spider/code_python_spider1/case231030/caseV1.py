# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 10:49
# @File    ：case231030.py
# @Function: RacingFactor 竞速因子

import datetime
import pandas as pd
from item import Item  # 导入Item类

FILE_NAME = f'RacingFactor{datetime.datetime.now().strftime("%y%m%d")}.csv'
items_list = []
items_list.append(Item("pythonWeb--：建立竞速因子系统", 18))

# 将Item对象的属性保存到DataFrame中
data = []
for item in items_list:
    data.append(item.get_attributes())
df = pd.DataFrame(data)

df.to_csv(FILE_NAME, index=False)  # 保存DataFrame为CSV文件
print(df)  # 打印DataFrame
