# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/30 15:27
# @File    ：office1v3_extract_file.py
# @Function: 按照时间顺序解压

import os
import glob
import zipfile
import rarfile
import py7zr


def extract_zip_with_encoding(zip_path, extract_to, encoding='cp936'):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # 提取ZIP文件前，将文件名编码转换为正确的格式
        for file in zip_ref.namelist():
            zip_ref.extract(file, extract_to)
            # 原始路径（可能有乱码）
            original_path = os.path.join(extract_to, file)
            # 转换后的路径
            correct_path = os.path.join(extract_to, file.encode('cp437').decode(encoding))
            # 重命名文件
            os.rename(original_path, correct_path)


def extract_file(file_path, extract_to):
    # 根据文件扩展名选择不同的解压方法
    if file_path.endswith('.zip'):
        extract_zip_with_encoding(file_path, extract_to)
    elif file_path.endswith('.rar'):
        with rarfile.RarFile(file_path, 'r') as rar_ref:
            rar_ref.extractall(extract_to)
    elif file_path.endswith('.7z'):
        with py7zr.SevenZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    else:
        print(f"F Unsupported file type: {file_path}")


def extract_all_files_in_directory(directory, extract_to=None):
    if extract_to is None:
        extract_to = directory

    # 支持的文件扩展名
    extensions = ['*.zip', '*.rar', '*.7z']

    # 获取文件列表并按创建时间排序
    file_list = []
    for extension in extensions:
        for file_path in glob.glob(os.path.join(directory, extension)):
            file_list.append(file_path)
    file_list.sort(key=lambda x: os.path.getctime(x))

    for file_path in file_list:
        try:
            extract_file(file_path, extract_to)
            os.remove(file_path)
            print(f'S Extracted {file_path} to {extract_to}')
            print(f"S Deleted the compressed file: {file_path}")
        except PermissionError:
            print(f"F Permission error: Unable to delete {file_path}. It may be in use by another program.")


if __name__ == '__main__':
    # 使用示例 - 请根据需要修改路径
    directory_to_search = r'C:\Users\huangyingzhu\Desktop\test2'  # 需要搜索的目录
    extract_directory = r'C:\Users\huangyingzhu\Desktop\test2e'  # 解压到哪个目录
    extract_all_files_in_directory(directory_to_search, extract_directory)
