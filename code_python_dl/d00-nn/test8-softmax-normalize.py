# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/22 9:26
# @File    ：test8-softmax-normalize.py
# @Function:

import numpy as np


# 标准化函数  防止梯度消失梯度爆炸
def normalize(arr):
    max_number = np.max(np.absolute(arr), axis=1, keepdims=True)
    scale_rate = np.where(max_number == 0, 1, 1 / max_number)  # 特殊情况考虑
    norm = arr * scale_rate
    return norm


# 激活函数softmax(最后一层 概率和为1)
def activation_softmax(inputs):
    # 指数平滑
    max_values = np.max(inputs, axis=1, keepdims=True)
    slided_inputs = inputs - max_values  # 平滑 防止数字过大内存溢出(稍微丢失点精度)
    exp_values = np.exp(slided_inputs)  # 指数运算 除减互换
    print('\n最大值结果')
    print(max_values)
    print('\n平滑结果')
    print(slided_inputs)
    print('\n指数平滑结果')
    print(exp_values)
    # 归一化  概率和为1
    norm_base = np.sum(exp_values, axis=1, keepdims=True)
    norm_values = exp_values / norm_base
    print('\n归一化结果')
    print(norm_values)
    return norm_values


inputs = np.array([[1, 0.2], [2, 0.3], [-0.9, 0.1], [-4, 3.2]])
print(inputs)

activation_softmax(inputs)
