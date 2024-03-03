# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/30 16:30
# @File    ：demo1.py
# @Function:

from office1v1_extract_file import *

directory_to_search = r'C:\Users\huangyingzhu\Desktop\test2'  # 需要搜索的目录
extract_directory = r'C:\Users\huangyingzhu\Desktop\test2e'  # 解压到哪个目录
extract_all_files_in_directory(directory_to_search, extract_directory)
