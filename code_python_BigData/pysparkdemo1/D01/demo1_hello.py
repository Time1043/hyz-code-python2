# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/7 14:30
# @File    ：demo1_hello.py
# @Function:

import os
from pyspark import SparkConf, SparkContext

# 临时设置环境变量  尽量不用win
# os.environ['PYSPARK_PYTHON'] = r'D:\systemEnvironment\Anaconda3\envs\pyspark\python.exe'

if __name__ == '__main__':
    # 通过SparkConf对象构建SparkContext对象
    conf = SparkConf().setMaster('local[*]').setAppName('wordCountHelloWorld')
    sc = SparkContext(conf=conf)
    # 读取文件 加载数据
    # file_rdd = sc.textFile('hdfs://node1:8020/test/input/wc2.txt')
    file_rdd = sc.textFile('../data/input/words.txt')

    # 单词切割 -> 存储单词的集合对象 -> kv  按k分组 对v聚合
    words_rdd = file_rdd.flatMap(lambda line: line.split(' '))
    words_with_one_rdd = words_rdd.map(lambda x: (x, 1))
    result_rdd = words_with_one_rdd.reduceByKey(lambda a, b: a + b)

    # 收集返回值
    print(result_rdd.collect())
