# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/10 8:30
# @File    ：demo2.py
# @Function:

import os
import re


def rename_folder_rm_num(path):
    for filename in os.listdir(path):
        if re.search(r'\d', filename):  # 使用正则表达式匹配数字
            new_filename = re.sub(r'\d', '', filename)  # 删除数字并重命名文件
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))


def count_files_and_rename_folders(path):
    for filename in os.listdir(path):
        if os.path.isdir(os.path.join(path, filename)):  # 判断是否为文件夹
            count = len([f for f in os.listdir(os.path.join(path, filename)) if
                         os.path.isfile(os.path.join(path, filename, f))])  # 计算文件夹中的文件数量
            new_filename = filename + str(count)  # 根据文件数量生成新的文件夹名
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))  # 重命名文件夹


if __name__ == '__main__':
    # rename_folder_rm_num(r'C:\Users\16654\Desktop\train')
    # count_files_and_rename_folders(r'C:\Users\16654\Desktop\train')

    rename_folder_rm_num(r'C:\Users\16654\Desktop\train\dataset2')
    # count_files_and_rename_folders(r'C:\Users\16654\Desktop\train\dataset2')
