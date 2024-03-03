# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/23 12:14
# @File    ：demo19.py
# @Function: 番外(多种图形)

import copy  # 拷贝一般对象 深度网络对象
import math
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
    if CLAIFICATION_TYOE == 'circle':
        tag = 0 if x ** 2 + y ** 2 < 1 else 1
    if CLAIFICATION_TYOE == 'ring':
        tag = 0 if x ** 2 + y ** 2 > 1 and x ** 2 + y ** 2 < 2 else 1
    if CLAIFICATION_TYOE == 'line':
        tag = 0 if x > 1 else 1
    if CLAIFICATION_TYOE == 'cross':
        tag = 0 if x * y > 0 else 1
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


# (一维的)标准化函数  防止梯度消失梯度爆炸
def vector_normalize(arr):
    max_number = np.max(np.absolute(arr))
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


# 不那么苛刻的损失函数(先四舍五入)
def loss_function(predicted, real):  # 预测的 标答的
    # 先四舍五入
    condition = (predicted > 0.5)
    binary_predicted = np.where(condition, 1, 0)  # 非零即一
    # 一样的计算损失
    real_matrix = np.zeros((len(real), 2))  # 构造形状
    real_matrix[:, 1], real_matrix[:, 0] = real, 1 - real  # 互补的
    product = np.sum(binary_predicted * real_matrix, axis=1)  # 衡量相似程度
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

    def network_backward(self, network_outputs, target_vector):  # 所有层的输出值(列表)  目标向量/标答
        backup_network = copy.deepcopy(self)  # 备用网络  各种参数都需要更新  作比较更好就代替否则不
        preAct_demands = get_finalLayer_preAct_demands(network_outputs[-1], target_vector)  # 最后的输出和标答比较 得到最后一层的需求值

        # 迭代循环  5层神经元  4层权重矩阵【0 1 2 3】
        for i in range(len(self.layers)):  # len=4    每一个Layer实际上代表两个连续的神经元层之间的连接
            layer = backup_network.layers[len(self.layers) - 1 - i]  # 【3 2 1 0】  反向传播的倒序处理

            if i != 0:  # 偏置项值  不修正最后一层  防止出现过拟合
                layer.biases += LEARNING_RATE * np.mean(preAct_demands, axis=0)  # 把所有条的特征i取平均  学习率
                layer.biases = vector_normalize(layer.biases)  # 标准化

            # 更新权重矩阵  迭代层的反向传播！！！
            outputs = network_outputs[len(network_outputs) - 2 - i]  # 【】【倒数第一层的需求值 倒数第二层的输出值】
            weight_adjust_matrix, preAct_demands = layer.layer_backward(outputs,
                                                                        preAct_demands)  # 迭代更新！！！  故意重名的preAct_demands
            # 该层的权重参数调整
            layer.weights += LEARNING_RATE * weight_adjust_matrix
            layer.weights = normalize(layer.weights)  # 标准化

        return backup_network  # 经过更新的神经网络

    def one_batch_train(self, batch):  # 单批次训练
        global force_train, random_train, n_improved, n_not_improved

        # 读取数据：一张矩阵(两列特征 一列标答)
        data_feature = batch[:, :2]  # 两个特征维度
        data_label = np.copy(batch[:, 2]).astype(int)  # 标答 标签
        # 前向传播
        outputs = self.network_forward(inputs=data_feature)  # 输出值列表 每一层的输出值
        precise_loss = precise_loss_function(outputs[-1], data_label)  # 计算损失函数
        loss = loss_function(outputs[-1], data_label)  # 容错的损失函数

        if np.mean(precise_loss) <= 0.1:  # 很准了不用再训练了
            print('No need for training! ')
        else:
            backup_network = self.network_backward(outputs, data_label)  # 备用网络
            backup_outputs = backup_network.network_forward(data_feature)  # 备用网络的前馈运算
            backup_precise_loss = precise_loss_function(backup_outputs[-1], data_label)
            backup_loss = loss_function(backup_outputs[-1], data_label)

            # 原来loss>新loss 训练成功 模型参数更新
            if np.mean(precise_loss) > np.mean(backup_precise_loss) or np.mean(loss) > np.mean(backup_loss):
                for i in range(len(self.layers)):
                    self.layers[i].weights = backup_network.layers[i].weights.copy()
                    self.layers[i].biases = backup_network.layers[i].biases.copy()
                print('Improved! ')
                n_improved += 1
            else:
                # 强制更新
                if force_train:
                    print('网络进行强制更新！')
                    for i in range(len(self.layers)):
                        self.layers[i].weights = backup_network.layers[i].weights.copy()
                        self.layers[i].biases = backup_network.layers[i].biases.copy()
                # 随即更新
                if random_train:
                    print('网络进行随机更新！')
                    self.random_update()
                else:
                    print('No improvement! ')
                    n_not_improved += 1
        print('----------------------------------------------------------------------------------')

    def random_update(self):  # 网络死亡 随即更新
        random_network = Network(NETWORK_SHAPE)
        # 对网络每层的参数都进行更新
        for i in range(len(self.layers)):
            weights_change, biases_change = random_network.layers[i].weights, random_network.layers[i].biases
            self.layers[i].weights += weights_change
            self.layers[i].biases += biases_change

    def train(self, n_entries):  # 多批次训练
        # 一些补救：遇到网络死亡
        global force_train, random_train, n_improved, n_not_improved
        n_improved, n_not_improved = 0, 0  # 归零

        n_batches = math.ceil(n_entries / BATCH_SIZE)  # 天花板除 向上取整
        for i in range(n_batches):
            batch = create_data(BATCH_SIZE)
            self.one_batch_train(batch)

        # 计算优化率
        improvement_rate = n_improved / (n_improved + n_not_improved)
        print('\n优化率')
        print(format(improvement_rate, '.0%'))
        # 强制更新 随即更新
        force_train = True if improvement_rate < 0.05 else False
        random_train = True if n_improved == 0 else False  # 网络死亡

        # 新生成一些数据去测试
        data = create_data(SAMPLES)
        plot_data(data, '正确的分类')
        # 测试展示
        inputs = data[:, :2]
        outputs = self.network_forward(inputs)
        classification = classify(outputs[-1])
        pre_data = np.copy(data)
        pre_data[:, 2] = classification
        plot_data(pre_data, '训练后的分类')


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
    LEARNING_RATE = 0.0003  # 学习率 炼丹炉  参数搜索

    # 一些补救：遇到网络死亡
    force_train = False  # 强制更新
    random_train = False  # 随即更新
    n_improved = 0  # 记录优化次数
    n_not_improved = 0  # 记录没有优化的次数

    # 数据
    CLAIFICATION_TYOE = 'ring'
    N_INPUTS = 2  # 输入的特征维度  第一层神经元的个数
    SAMPLES = 2000  # 样本个数  输入矩阵的行数
    BATCH_SIZE = 40  # 一批一批地送入
    data = create_data(SAMPLES)
    plot_data(data, '原始数据情况')

    # 实例化网络对象
    NETWORK_SHAPE = [N_INPUTS, 260, 400, 300, 350, 340, 280, 2]

    # 起始网络选择  while
    use_this_network = 'n'
    while use_this_network != 'Y':
        network = Network(NETWORK_SHAPE)

        # 训练前的展示
        inputs = data[:, :2]
        outputs = network.network_forward(inputs)
        classification = classify(outputs[-1])
        data[:, 2] = classification
        plot_data(data, '训练前的分类')

        use_this_network = input('Use this network? Y or n\n')

    # 训练的控制
    do_train = input('Train? Y or n 接受直接输入训练数据的条数\n')
    while do_train == 'Y' or do_train.isnumeric() == True:
        if do_train.isnumeric() == True:
            n_entries = int(do_train)
        else:
            n_entries = int(inputs('输入训练数据的条数\n'))
        network.train(n_entries)  # 多批次训练
        do_train = input('Train? Y or n 接受直接输入训练数据的条数\n')

    # 演示训练效果
    inputs = data[:, :2]
    outputs = network.network_forward(inputs)
    classification = classify(outputs[-1])
    data[:, 2] = classification
    plot_data(data, '训练后的分类')
