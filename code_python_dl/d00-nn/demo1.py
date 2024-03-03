# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/21 19:51
# @File    ：demo1.py
# @Function: 一个神经元(线性函数计算、激活函数输出)

import numpy as np

# 具体化输入值
x1, x2, x3 = 0.1, -0.2, 0.9
# 具体化权重值
w1, w2, w3 = 0.6, 0.5, -0.3
# 具体化偏置项
b1 = 0.22

# 线性函数计算
output1 = w1 * x1 + w2 * x2 + w3 * x3 + b1
print(output1)  # -0.09000000000000005
# 激活函数输出
print(np.maximum(0, output1))  # 0.0
