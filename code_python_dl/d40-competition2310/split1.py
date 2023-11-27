# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/13 12:09
# @File    ：split1.py
# @Function:

import os
import shutil
from sklearn.model_selection import train_test_split


dataset_dir = r'C:\Users\16654\Desktop\train\dataset2'
split_dataset_dir = r'C:\Users\16654\Desktop\train\dataset2_split'
os.makedirs(split_dataset_dir, exist_ok=True)

# 获取所有类别的文件夹名称
class_names = os.listdir(dataset_dir)
# 循环处理每个类别
for class_name in class_names:
    class_dir = os.path.join(dataset_dir, class_name)
    # 获取该类别下所有图像文件
    image_files = [f for f in os.listdir(class_dir) if f.endswith('.jpg')]
    # 随机划分为训练集和测试集
    train_files, test_files = train_test_split(image_files, test_size=0.2, random_state=42)
    # 创建训练集和测试集子文件夹
    train_dir = os.path.join(split_dataset_dir, 'train', class_name)
    test_dir = os.path.join(split_dataset_dir, 'test', class_name)
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    # 移动图像文件到相应的子文件夹
    for train_file in train_files:
        src = os.path.join(class_dir, train_file)
        dst = os.path.join(train_dir, train_file)
        shutil.copy(src, dst)
    for test_file in test_files:
        src = os.path.join(class_dir, test_file)
        dst = os.path.join(test_dir, test_file)
        shutil.copy(src, dst)
print("数据集划分完成")
