# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/30 16:01
# @File    ：office1v2_extract_file.py
# @Function:

import os
import glob
import zipfile
import rarfile
import py7zr


def create_folder_if_needed(member_list, extract_to):
    """如果需要，为压缩包内的文件创建一个新文件夹"""
    if member_list and '/' not in member_list[0] and '\\' not in member_list[0]:
        # 创建以第一个文件名（去掉扩展名）为名的新文件夹
        folder_name = os.path.splitext(member_list[0])[0]
        new_extract_to = os.path.join(extract_to, folder_name)
        os.makedirs(new_extract_to, exist_ok=True)
        return new_extract_to
    return extract_to


def extract_compressed_file(file_path, extract_to, encoding='cp936'):
    """解压压缩文件（支持zip, rar, 7z格式）"""
    if file_path.endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            member_list = zip_ref.namelist()
            new_extract_to = create_folder_if_needed(member_list, extract_to)
            for file in member_list:
                zip_ref.extract(file, new_extract_to)
                original_path = os.path.join(new_extract_to, file)
                correct_path = os.path.join(new_extract_to, file.encode('cp437').decode(encoding))
                os.rename(original_path, correct_path)
    elif file_path.endswith('.rar'):
        with rarfile.RarFile(file_path, 'r') as rar_ref:
            member_list = rar_ref.namelist()
            new_extract_to = create_folder_if_needed(member_list, extract_to)
            rar_ref.extractall(new_extract_to)
    elif file_path.endswith('.7z'):
        with py7zr.SevenZipFile(file_path, 'r') as zip_ref:
            member_list = zip_ref.getnames()
            new_extract_to = create_folder_if_needed(member_list, extract_to)
            zip_ref.extractall(new_extract_to)
    else:
        print(f"Unsupported file type: {file_path}")


def extract_all_files_in_directory(directory, extract_to=None):
    if extract_to is None:
        extract_to = directory

    # 支持的文件扩展名
    extensions = ['*.zip', '*.rar', '*.7z']

    # 对于每种扩展名，找到匹配的文件并解压
    for extension in extensions:
        for file_path in glob.glob(os.path.join(directory, extension)):
            extract_compressed_file(file_path, extract_to)
            print(f'Extracted {file_path} to {extract_to}')


if __name__ == '__main__':
    # 使用示例 - 请根据需要修改路径
    directory_to_search = r'C:\Users\huangyingzhu\Desktop\test2'  # 需要搜索的目录
    extract_directory = r'C:\Users\huangyingzhu\Desktop\test2e'  # 解压到哪个目录
    extract_all_files_in_directory(directory_to_search, extract_directory)
