# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/21 21:34
# @File    ：demo6.py
# @Function: 面向对象的层(简化层的参数和运算)

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


class Layer:  # 参数 (输出) 运算
    def __init__(self, n_inputs, n_neurons):  # 初始化属性
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.random.randn(n_neurons)
        self.outputs = None

    def layer_forward(self, inputs):  # 向前运算
        sum_i = np.dot(inputs, self.weights) + self.biases  # 线性函数计算
        self.outputs_i = activation_ReLU(sum_i)  # 激活函数输出
        return self.outputs_i


if __name__ == '__main__':
    np.random.seed(43)  # 随机种子

    # 输入矩阵
    inputs = create_inputs(4)

    # 参数 实例化层对象
    layer1 = Layer(3, 4)
    layer2 = Layer(4, 3)
    layer3 = Layer(3, 2)

    # 运算
    outputs_1 = layer1.layer_forward(inputs)
    outputs_2 = layer2.layer_forward(outputs_1)
    outputs_3 = layer3.layer_forward(outputs_2)

    # 结果是4个实例
    print('第一层运算结果：\n', outputs_1)
    print('第二层运算结果：\n', outputs_2)
    print('第三层运算结果：\n', outputs_3)
