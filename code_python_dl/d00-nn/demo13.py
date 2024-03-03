# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/22 17:28
# @File    ：demo13.py
# @Function: 层的反向传播

import pprint
import warnings
import numpy as np
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")  # 抑制所有警告
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号


# 生成输入矩阵：可指定输入的特征维度 可指定实例数量  4个实例
def create_inputs(samples, n_inputs=2):
    colunms = [np.random.uniform(-2, 2, samples) for _ in range(n_inputs)]
    return np.column_stack(colunms)


# 一个条目的标签  二维空间的二分类 决策边界是圆
def tag_entry(x, y):
    tag = 0 if x ** 2 + y ** 2 < 1 else 1
    return tag


# 生成数据 (特征+标答=增广)  两个特征维度
def create_data(samples):
    entries_list = []
    feature_entries = create_inputs(samples)
    for i in range(samples):
        x, y = feature_entries[i][0], feature_entries[i][1]
        tag = tag_entry(x, y)  # 标答
        entry = [x, y, tag]  # 增广矩阵
        entries_list.append(entry)
    return np.array(entries_list)


# 对生成数据的可视化
def plot_data(data, title):
    plt.figure(figsize=(4, 4))  # 设置图像大小
    color = []
    for i in data[:, 2]:  # 标签为0是橙色 标签为1是蓝色
        color = ['orange' if i == 0 else 'blue' for i in data[:, 2]]
    plt.scatter(data[:, 0], data[:, 1], c=color, s=3)
    plt.title(title)
    plt.show()


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


# 分类函数 将softmax的概率值转换为分类标签  与题目的增广矩阵对应
def classify(probabilities):
    # 两个和为1的概率值 只看第二个概率值
    classification = np.rint(probabilities[:, 1])  # 四舍五入
    return classification


# 知错的损失函数：用点乘衡量两组数据的相似程度
def precise_loss_function(predicted, real):  # 预测的 标答的
    real_matrix = np.zeros((len(real), 2))  # 构造形状
    real_matrix[:, 1], real_matrix[:, 0] = real, 1 - real  # 互补的
    product = np.sum(predicted * real_matrix, axis=1)  # 衡量相似程度
    return 1 - product  # 损失函数越大准确性越差


# 最后一层的需求函数(在激活函数之前)
def get_finalLayer_preAct_demands(predicted_values, target_vector):  # 预测的 标答的
    target_matrix = np.zeros((len(target_vector), 2))  # 构造形状
    target_matrix[:, 1], target_matrix[:, 0] = target_vector, 1 - target_vector  # 互补的
    # 每一条数据的运算
    for i in range(len(target_vector)):
        target_matrix[i] = np.array([0, 0]) if np.dot(target_matrix[i], predicted_values[i]) > 0.5 else (target_matrix[
                                                                                                             i] - 0.5) * 2
    return target_matrix


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
            layer_outputs = normalize(activation_ReLU(layer_outputs_linear)) if i < len(
                self.layers) - 1 else activation_softmax(layer_outputs_linear)
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

    def layer_backward(self, preWeights_values, afterWeights_demands):  # 权重矩阵之前的输出值(已知) 权重矩阵之后的需求值(已知)【传播】
        # 【求权重矩阵之前的需求值】
        preWeights_demands = np.dot(afterWeights_demands, self.weights.T)  # 反向传播 需要转置
        # 激活函数求导  分段函数的条件
        condition = (preWeights_values > 0)
        value_derivatives = np.where(condition, 1, 0)  # if一条 np.where整个矩阵都处理
        # 【求激活函数之前的需求值】
        preActs_demands = value_derivatives * preWeights_demands
        # 标准化  一层一层地传递容易出现发散或收敛  梯度消失或梯度爆炸
        norm_preActs_demands = normalize(preActs_demands)

        # 调整矩阵 标准化
        weight_adjust_matrix = self.get_weight_adjust_matrix(preWeights_values, afterWeights_demands)
        norm_weight_adjust_matrix = normalize(weight_adjust_matrix)

        return (norm_weight_adjust_matrix, norm_preActs_demands)  # 权重调整矩阵 激活函数之前的需求值  【闭环】

    def get_weight_adjust_matrix(self, preWeights_values, aftWeights_demands):  # 权重调整矩阵 两个向量相乘(前一个的输出值 后一个的需求值)
        # 构造矩阵
        plain_weights = np.ones_like(self.weights)  # 和权重矩阵的形状一样
        weight_adjust_matrix = np.zeros_like(self.weights)  # 和权重矩阵的形状一样  很多条数据 权重调整矩阵需求平均
        # 运算：((全1矩阵.T * 前一个输出矩阵).T * 后一个需求)   后求和再求平均
        for i in range(BATCH_SIZE):  # 批量处理数据  每一条都要进行如下运算
            weight_adjust_matrix += (plain_weights.T * preWeights_values[i, :]).T * aftWeights_demands[i,
                                                                                    :]  # 第i行的所有列 体现每一条数据
        weight_adjust_matrix = weight_adjust_matrix / BATCH_SIZE  # 求和后除数量  即求平均
        return weight_adjust_matrix


if __name__ == '__main__':
    np.random.seed(43)  # 随机种子

    # 数据 输入矩阵
    N_INPUTS = 2  # 输入的特征维度  第一层神经元的个数
    SAMPLES = 20  # 样本个数  输入矩阵的行数
    BATCH_SIZE = SAMPLES  # 一批一批地送入
    data = create_data(SAMPLES)
    plot_data(data, '原始数据情况')

    data_feature = np.copy(data[:, :2])  # 两个特征维度
    data_label = np.copy(data[:, 2])  # 标答 标签
    print('\n标答的标签')
    print(data_label)

    # 参数 实例化网络对象
    NETWORK_SHAPE = [N_INPUTS, 4, 3, 2]
    network = Network(NETWORK_SHAPE)
    # 前向运算
    outputs = network.network_forward(data_feature)  # 两个特征维度
    # 输出层的概率结果
    print('\n预测的概率')
    pprint.pprint(outputs[-1])

    # 分类函数：将概率值转化为标签
    classification = classify(outputs[-1])
    print('\n预测的概率转化为标签(本次不用)')
    print(classification)
    pre0_data = np.copy(data)
    pre0_data[:, 2] = classification  # 第一次对标签的预测情况
    plot_data(pre0_data, '还没训练的预测情况')  # 瞎蒙的

    # 用预测的概率值(不用分类标签)求损失
    loss = precise_loss_function(outputs[-1], data_label)
    print('\n损失')
    print(loss)

    # 用预测的概率值(不用分类标签)求需求
    demands = get_finalLayer_preAct_demands(outputs[-1], data_label)
    print('\n需求(希望每条数据的z值怎么变：增大、缩小、不变)')
    print(demands)

    # 最后一层的调整矩阵  network.layers[-1]
    adjust_matrix = network.layers[-1].get_weight_adjust_matrix(outputs[-2], demands)  # outputs[-2] 前一个输出(即倒数第二)
    print('\n权重调整矩阵(权重参数矩阵应该怎么变)')
    print(adjust_matrix)

    # 最后一层的反向传播
    layer_backward = network.layers[-1].layer_backward(outputs[-2], demands)
    print('\n最后一层的反向传播的结果(权重调整矩阵/上面已有/加上标准化、激活函数之前的需求值/权重矩阵之后的需求值)')
    pprint.pprint(layer_backward)
