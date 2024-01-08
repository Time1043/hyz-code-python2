# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/7 15:09
# @File    ：demo2_hello.py
# @Function:

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    # Driver
    conf = SparkConf().setAppName('wordCountHelloWorld')  # yarn
    sc = SparkContext(conf=conf)

    # Executor * 3
    file_rdd = sc.textFile('hdfs://node1:8020/test/input/wc2.txt')  # hdfs
    result_rdd = file_rdd.flatMap(lambda line: line.split(' ')) \
        .map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)

    # Driver
    print(result_rdd.collect())
