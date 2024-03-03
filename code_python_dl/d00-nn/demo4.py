# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/21 20:51
# @File    ：demo4.py
# @Function: 不再具体值，而是规模化随机生成值(2参数矩阵 输入矩阵)

import numpy as np


# 固定三个特征维度 可指定实例数量  4个实例
def create_inputs(smaple):
    heights = np.random.uniform(150, 200, smaple)  # 身高在150到200之间的随机数
    weights = np.random.uniform(40, 100, smaple)  # 体重在40到100之间的随机数
    ages = np.random.randint(18, 80, smaple)  # 年龄在18到80之间的随机整数
    return np.column_stack((heights, weights, ages))  # 将身高、体重和年龄堆叠成一个二维数组


# 生成权重参数矩阵
def create_weights(n_inputs, n_neurons):
    return np.random.randn(n_inputs, n_neurons)


# 生成偏置参数矩阵
def create_biases(n_neurons):
    return np.random.randn(n_neurons)


# 激活函数ReLU(除最后一层外)
def activation_ReLU(inputs):
    return np.maximum(0, inputs)


if __name__ == '__main__':
    np.random.seed(43)  # 随机种子

    # 输入矩阵
    inputs = create_inputs(4)

    # 权重矩阵
    weights = create_weights(3, 2)
    # 偏置矩阵
    b = create_biases(2)

    # 线性函数计算
    outputs = np.dot(inputs, weights) + b
    # 激活函数输出
    print(activation_ReLU(outputs))  # 结果是4个实例
