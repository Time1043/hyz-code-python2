# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/22 7:58
# @File    ：demo3-2.py
# @Function: 两个神经元(输入矩阵batch)

import numpy as np

# 具体化输入值  4个实例
x11, x12, x13 = 0.1, -0.2, 0.9
x21, x22, x23 = 1, -0.2, 3.9
x31, x32, x33 = 0.1, -3.2, -0.9
x41, x42, x43 = 0.44, 0.2, 0.1
x1 = np.array([x11, x12, x13])
x2 = np.array([x21, x22, x23])
x3 = np.array([x31, x32, x33])
x4 = np.array([x41, x42, x43])
# 具体化权重值  两个神经元
w11, w21, w31 = 0.6, 0.5, -0.3
w12, w22, w32 = 6, 0.5, -0.3
# 具体化偏置项  两个神经元
b1 = 0.22
b2 = 0.22


# 激活函数ReLU(除最后一层外)
def activation_ReLU(inputs):
    return np.maximum(0, inputs)


# 矩阵形式的输入值
inputs = np.array([x1, x2, x3, x4])  # 4个实例
# 矩阵形式的权重值
weights = np.array([[w11, w12], [w21, w22], [w31, w32]])
# 矩阵形式的偏置项
b = np.array([b1, b2])

# 线性函数计算
outputs = np.dot(inputs, weights) + b
# 激活函数输出
print(activation_ReLU(outputs))  # 结果是4个实例
