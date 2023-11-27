# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/22 9:50
# @File    ：test9-data.py
# @Function:

import warnings
import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")  # 抑制所有警告
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号


# 生成输入矩阵：可指定输入的特征维度 可指定实例数量  4个实例
def create_inputs(samples, n_inputs=2):
    colunms = [np.random.uniform(-2, 2, samples) for _ in range(n_inputs)]
    return np.column_stack(colunms)


# 一个条目的标签  二维空间的二分类 决策边界是圆
def tag_entry(x, y):
    tag = 0 if x ** 2 + y ** 2 < 1 else 1
    return tag


# 生成数据
def create_data(samples):
    entries_list = []
    feature_entries = create_inputs(samples)
    print('\n特征矩阵')
    print(feature_entries)

    for i in range(samples):
        x, y = feature_entries[i][0], feature_entries[i][1]
        tag = tag_entry(x, y)  # 标答
        entry = [x, y, tag]  # 增广矩阵
        entries_list.append(entry)

    print('\n增广矩阵')
    print(np.array(entries_list))
    return np.array(entries_list)


# 对生成数据的可视化
def plot_data(data, title):
    plt.figure(figsize=(4, 4))  # 设置图像大小
    color = []
    for i in data[:, 2]:  # 标签为0是橙色 标签为1是蓝色
        color = ['orange' if i == 0 else 'blue' for i in data[:, 2]]
    plt.scatter(data[:, 0], data[:, 1], c=color, s=3)
    plt.title(title)
    plt.show()


SAMPLES = 400  # 样本数目
data = create_data(SAMPLES)
plot_data(data, '原始数据情况')
