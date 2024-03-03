# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/22 10:54
# @File    ：test10-classify.py
# @Function:

import numpy as np


# 分类函数 将softmax的概率值转换为分类标签  与题目的增广矩阵对应
def classify(probabilities):
    # 两个和为1的概率值 只看第二个概率值
    classification = np.rint(probabilities[:, 1])  # 四舍五入
    return classification


probabilities = np.array([[6.89974481e-01, 3.10025519e-01],
                          [8.45534735e-01, 1.54465265e-01],
                          [2.68941421e-01, 7.31058579e-01],
                          [7.46028834e-04, 9.99253971e-01]])
print(classify(probabilities))
