# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/21 21:12
# @File    ：demo5.py
# @Function: 从一层神经网络到多层神经网络

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

    # 第一层的参数
    weights_1 = create_weights(3, 4)
    biases_1 = create_biases(4)
    # 第二层的参数
    weights_2 = create_weights(4, 3)
    biases_2 = create_biases(3)
    # 第三层的参数
    weights_3 = create_weights(3, 2)
    biases_3 = create_biases(2)

    # 第一层运算
    sum_1 = np.dot(inputs, weights_1) + biases_1
    outputs_1 = activation_ReLU(sum_1)
    # 第二层运算
    sum_2 = np.dot(outputs_1, weights_2) + biases_2
    outputs_2 = activation_ReLU(sum_2)
    # 第三层运算
    sum_3 = np.dot(outputs_2, weights_3) + biases_3
    outputs_3 = activation_ReLU(sum_3)

    # 结果是4个实例
    print('第一层运算结果：\n', outputs_1)
    print('第二层运算结果：\n', outputs_2)
    print('第三层运算结果：\n', outputs_3)
