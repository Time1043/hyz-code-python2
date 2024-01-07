# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/27 19:31
# @File    ：demo1.py
# @Function: 将pdf和mp3文件分开


import os
import shutil

# 设置原始文件夹和目标文件夹路径
source_dir = r'C:\Users\16654\Desktop\dedao\2312谷歌方法论'
target_dir = r'C:\Users\16654\Desktop\dedao\2312谷歌方法论\文章'

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 遍历原始文件夹中的所有文件
for file in os.listdir(source_dir):
    # 检查文件是否是PDF
    if file.lower().endswith('.pdf'):
        # 构建原始和目标文件的完整路径
        source_file = os.path.join(source_dir, file)
        target_file = os.path.join(target_dir, file)

        # 移动文件
        shutil.move(source_file, target_file)
        print(f"Moved: {file}")

# 打印完成的消息
print("All PDF files have been moved to the '文章' directory.")
