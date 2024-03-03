# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/8 23:36
# @File    ：demo12_broadcast_accumulator.py
# @Function:

import re

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('broadcast_accumulator').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    file_rdd = sc.textFile('../data/input/accumulator_broadcast_data.txt')
    abnormal_char = [',', '.', '!', '#', '$', '%']
    broadcast = sc.broadcast(abnormal_char)  # 广播变量
    acmlt = sc.accumulator(0)  # 累加器

    lines_rdd = file_rdd.filter(lambda line: line.strip())  # 过滤空行 有内容是True没内容是False
    data_rdd = lines_rdd.map(lambda line: line.strip())  # 去除了前后空格
    words_rdd = data_rdd.flatMap(lambda line: re.split('\s+', line))  # 对数据切分 正则
