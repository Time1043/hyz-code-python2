# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/22 9:03
# @File    ：demo8.py
# @Function: 反向传播的准备 (激活函数softmax) (ReLU需要标准化函数) (激活函数运算归网络对象)

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


# 标准化函数  防止梯度消失梯度爆炸
def normalize(arr):
    max_number = np.max(np.absolute(arr), axis=1, keepdims=True)
    scale_rate = np.where(max_number == 0, 1, 1 / max_number)  # 特殊情况考虑
    norm = arr * scale_rate
    return norm


# 激活函数ReLU(除最后一层外)
def activation_ReLU(inputs):
    return np.maximum(0, inputs)


# 激活函数softmax(最后一层 概率和为1)
def activation_softmax(inputs):
    # 指数平滑
    max_values = np.max(inputs, axis=1, keepdims=True)
    slided_inputs = inputs - max_values  # 平滑 防止数字过大内存溢出(稍微丢失点精度)
    exp_values = np.exp(slided_inputs)  # 指数运算 除减互换
    # 归一化  概率和为1
    norm_base = np.sum(exp_values, axis=1, keepdims=True)
    norm_values = exp_values / norm_base
    return norm_values


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
            layer_outputs_linear = self.layers[i].layer_forward(outputs[i])  # 线性函数运算  激活函数输出
            layer_outputs = normalize(activation_ReLU(layer_outputs_linear)) if i < len(self.layers) - 1 else activation_softmax(layer_outputs_linear)
            outputs.append(layer_outputs)
        return outputs


class Layer:  # 参数 (输出) 运算
    def __init__(self, n_inputs, n_neurons):  # 初始化属性
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.random.randn(n_neurons)
        self.outputs = None

    def layer_forward(self, inputs):  # 向前运算
        self.sum_i = np.dot(inputs, self.weights) + self.biases  # 线性函数计算
        return self.sum_i


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
