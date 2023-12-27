# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/22 9:48
# @File    ：demo2.py
# @Function:


import os

def list_file_names_in_directory(path):
    """ 列出给定目录路径及其子目录中的所有文件名称 """
    file_names = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_names.append(file)  # 仅添加文件名，不包括完整路径
    return file_names

# 示例使用
path = r'C:\Users\huangyingzhu\Desktop\Transformer'
file_names_only = list_file_names_in_directory(path)
# print(file_names_only)
for file_name in file_names_only:
    print(file_name)

