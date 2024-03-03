# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/21 22:06
# @File    ：demo7-2.py
# @Function: 面向对象的网络(规模化层) - 进一步规整(网络的前向传播运算) (输入矩阵指定特征维度)

import pprint
import numpy as np


# 生成输入矩阵：可指定输入的特征维度 可指定实例数量  4个实例
def create_inputs(samples, n_inputs):
    colunms = [np.random.randn(samples) for _ in range(n_inputs)]
    return np.column_stack(colunms)


# 生成权重参数矩阵
def create_weights(n_inputs, n_neurons):
    return np.random.randn(n_inputs, n_neurons)


# 生成偏置参数矩阵
def create_biases(n_neurons):
    return np.random.randn(n_neurons)


# 激活函数ReLU(除最后一层外)
def activation_ReLU(inputs):
    return np.maximum(0, inputs)


class Network:
    def __init__(self, network_shape):  # 网络的形状
        self.shape = network_shape
        self.layers = []  # 列表存储神经网络的参数 for
        for i in range(len(network_shape) - 1):  # 4层神经元 3层参数
            layer = Layer(network_shape[i], network_shape[i + 1])
            self.layers.append(layer)

    def network_forward(self, inputs):  # 最先的输入 然后传导
        outputs = [inputs]  # 把网络每层运算的输出规范成列表 for
        for i in range(len(self.layers)):
            layer_outputs = self.layers[i].layer_forward(outputs[i])  # outputs列表 运算需要
            outputs.append(layer_outputs)
        return outputs


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

    # 数据 输入矩阵
    N_INPUTS = 3  # 输入的特征维度  第一层神经元的个数
    SAMPLES = 4  # 样本个数  输入矩阵的行数
    inputs = create_inputs(SAMPLES, N_INPUTS)

    # 参数 实例化网络对象
    NETWORK_SHAPE = [N_INPUTS, 4, 3, 2]
    network = Network(NETWORK_SHAPE)
    # 运算
    outputs = network.network_forward(inputs)

    # 结果是4个实例
    pprint.pprint(outputs)
