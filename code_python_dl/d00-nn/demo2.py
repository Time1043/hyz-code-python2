# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/21 20:15
# @File    ：demo2.py
# @Function: 线性函数计算(矩阵向量)、激活函数输出(封装函数)

import numpy as np

# 具体化输入值
x1, x2, x3 = 0.1, -0.2, 0.9
# 具体化权重值
w1, w2, w3 = 0.6, 0.5, -0.3
# 具体化偏置项
b1 = 0.22


# 激活函数ReLU(除最后一层外)
def activation_ReLU(inputs):
    return np.maximum(0, inputs)


# 矩阵形式的输入值
inputs = np.array([x1, x2, x3])
# 矩阵形式的权重值
weights = np.array([[w1], [w2], [w3]])

# 线性函数计算
output1 = np.dot(inputs, weights) + b1
print(output1)  # [-0.09]
# 激活函数输出
print(activation_ReLU(output1))  # [0.]
