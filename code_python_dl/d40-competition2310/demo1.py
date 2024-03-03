# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/9 16:05
# @File    ：demo1.py
# @Function:

import os


def rename_images(folder_path):
    # 获取文件夹名称
    folder_name = os.path.basename(folder_path)
    # 获取文件夹内所有文件的路径
    files = os.listdir(folder_path)
    # 初始化计数器
    # count = 10000000
    count = 10000
    # count = 1

    for file in files:
        # 获取文件扩展名
        file_ext = os.path.splitext(file)[1]
        # 判断文件是否为图片文件
        if file_ext.lower() in ['.png', '.jpg']:
            # 构建新的文件名
            new_file_name = f"{folder_name}{count}{file_ext}"
            # 构建新的文件路径
            new_file_path = os.path.join(folder_path, new_file_name)
            # 原文件路径
            old_file_path = os.path.join(folder_path, file)
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            # 计数器自增
            count += 1


# 调用函数并传入文件夹路径
rename_images(r"D:\photo\钢笔")
