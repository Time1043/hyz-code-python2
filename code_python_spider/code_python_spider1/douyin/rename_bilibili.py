# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/30 0:13
# @File    ：rename_bilibili.py
# @Function:

import os
import pandas as pd
from datetime import datetime


def rename_data(file_name):
    # 设置数据文件夹和CSV文件的路径
    data_folder = fr'.\{file_name}\data'
    csv_file = fr'.\{file_name}\{file_name}.csv'

    df = pd.read_csv(csv_file, encoding='utf-8')  # 读取CSV文件
    for index, row in df.iterrows():  # 遍历CSV文件中的每一行
        # 获取视频标题和日期时间
        video_title = row['标题']
        date_str = row['日期时间']
        # 将日期时间转换为所需的格式
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        new_date_str = date.strftime('%y%m%d')

        new_file_name = f"【{new_date_str}】{video_title}.mp4"  # 构造新的文件名
        old_file_path = os.path.join(data_folder, f"{video_title}.mp4")  # 构造原文件名的完整路径

        try:
            if os.path.exists(old_file_path):  # 检查文件是否存在
                new_file_path = os.path.join(data_folder, new_file_name)  # 构造新文件名的完整路径
                os.rename(old_file_path, new_file_path)  # 重命名文件
            else:
                print(f"文件不存在：{old_file_path}")
        except Exception as e:
            print("请求过程中出现了一个异常:", e)


def rename_audio(file_name):
    # 设置数据文件夹和CSV文件的路径
    audio_folder = fr'.\{file_name}\audio'
    csv_file = fr'.\{file_name}\{file_name}.csv'

    df = pd.read_csv(csv_file, encoding='utf-8')  # 读取CSV文件
    for index, row in df.iterrows():  # 遍历CSV文件中的每一行
        # 获取视频标题和日期时间
        video_title = row['标题']
        date_str = row['日期时间']
        # 将日期时间转换为所需的格式
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        new_date_str = date.strftime('%y%m%d')

        new_file_name = f"【{new_date_str}】{video_title}.mp3"  # 构造新的文件名
        old_file_path = os.path.join(audio_folder, f"{video_title}.mp3")  # 构造原文件名的完整路径

        try:
            if os.path.exists(old_file_path):  # 检查文件是否存在
                new_file_path = os.path.join(audio_folder, new_file_name)  # 构造新文件名的完整路径
                os.rename(old_file_path, new_file_path)  # 重命名文件
            else:
                print(f"文件不存在：{old_file_path}")
        except Exception as e:
            print("请求过程中出现了一个异常:", e)


if __name__ == '__main__':
    rename_data('张志浩')
    rename_audio('张志浩')
