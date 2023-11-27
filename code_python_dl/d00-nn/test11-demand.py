# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/22 12:32
# @File    ：test11-demand.py
# @Function:

import numpy as np


# 需求函数(最后一层)
def get_finalLayer_preAct_demands(predicted_values, target_vector):  # 预测的 标答的
    target_matrix = np.zeros((len(target_vector), 2))  # 构造形状
    target_matrix[:, 1], target_matrix[:, 0] = target_vector, 1 - target_vector  # 互补的
    # 每一条数据的运算  若相似则[0,0]  若不相似则借1
    for i in range(len(target_vector)):
        target_matrix[i] = np.array([0, 0]) if np.dot(target_matrix[i], predicted_values[i]) > 0.5 else (target_matrix[i] - 0.5) * 2
    return target_matrix


predicted_values = np.array([[0.91202486, 0.08797514],
                             [0.91539237, 0.08460763],
                             [0.86425706, 0.13574294],
                             [0.91343251, 0.08656749],
                             [0.91590348, 0.08409652],
                             [0.91685808, 0.08314192],
                             [0.87685011, 0.12314989],
                             [0.91531129, 0.08468871],
                             [0.61268086, 0.38731914],
                             [0.90428019, 0.09571981],
                             [0.85898201, 0.14101799],
                             [0.91719511, 0.08280489],
                             [0.91490672, 0.08509328],
                             [0.90986069, 0.09013931],
                             [0.91607921, 0.08392079],
                             [0.91330785, 0.08669215],
                             [0.91464328, 0.08535672],
                             [0.91529745, 0.08470255],
                             [0.61268086, 0.38731914],
                             [0.89983567, 0.10016433]])
target_vector = np.array([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1])
print(get_finalLayer_preAct_demands(predicted_values, target_vector))
