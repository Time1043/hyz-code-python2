# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/22 13:02
# @File    ：test12-weight-adjust-matrix.py
# @Function:

import numpy as np


def get_weight_adjust_matrix(values, demands):  # 权重调整矩阵为：前一个输出 和 后一个需求 的乘积
    # 构造三个矩阵
    plain_weights = np.full((len(values), len(demands)), 1)  # 保证形状 花乘
    plain_weights_T = plain_weights.T
    print('\n全1矩阵(和权重矩阵形状一样)')
    print(plain_weights)
    print('\n全1矩阵的转置')
    print(plain_weights_T)
    print('\n前一个的输出矩阵')
    print(values)
    print('\n全1矩阵乘前一个输出矩阵')
    print(plain_weights_T * values)

    weight_adjust_matrix = (plain_weights_T * values).T * demands
    print('\n前一个输出和后一个需求的乘积(权重调整矩阵)')
    print(weight_adjust_matrix)

    return weight_adjust_matrix


# 测试调整矩阵的运算
values = np.array([1, 2, 3, 4])
demands = np.array([1, 2])
get_weight_adjust_matrix(values, demands)
