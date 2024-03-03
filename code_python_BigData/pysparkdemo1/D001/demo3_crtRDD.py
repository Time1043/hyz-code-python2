# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/7 19:30
# @File    ：demo3_crtRDD.py
# @Function:

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    # 程序入口
    conf = SparkConf().setAppName('crtRDD').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # 本地集合对象 -> rdd
    rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6])  # 参数1(集合对象list)  参数2(分区数 不写有默认)
    print(rdd1.getNumPartitions())  # 默认分区数是24
    print(rdd1.collect())  # 收集rdd内容 (分布式 -> 本地集合)

    # 从文件中获取rdd
    file_rdd = sc.textFile('../data/input/words.txt', 10000)  # 参数1(本地win linux hdfs)  参数2(最小分区数 可选且话语权不足)
    print(file_rdd.getNumPartitions())  # 默认分区数2 (与文件大小有关)
    print(file_rdd.collect())

    # 从一堆小文件中获取rdd
    file_rdd2 = sc.wholeTextFiles('../data/input/tiny_files')
    print(file_rdd2.collect())  # k-v 文件路径-文件内容  (数组)
    print(file_rdd2.map(lambda x: x[1]).collect())
