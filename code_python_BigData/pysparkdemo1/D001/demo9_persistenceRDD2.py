# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 14:18
# @File    ：demo9_persistenceRDD2.py.py
# @Function:

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('persistenceRDD2')
    sc = SparkContext(conf=conf)
    sc.setCheckpointDir('hdfs://node1:8020/test/output/bj52ckp')  # 选择cp保存路径

    rdd3 = sc.parallelize([3, 2, 6, 893, 23, 22], 3)
    rdd3.checkpoint()  # 使用
