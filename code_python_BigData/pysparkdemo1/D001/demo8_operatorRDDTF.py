# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 10:44
# @File    ：demo8_operatorRDDTF.py
# @Function:

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('operatorRDDTF')
    sc = SparkContext(conf=conf)


    # mapPartitions：一次处理的是一整个分区  (map是一条数据地处理)  【性能加强】
    rdd13 = sc.parallelize([3, 2, 6, 893, 23, 22], 3)
    def process(iter):
        result = list()
        for it in iter:
            result.append(it * 10)
        return result
    print(rdd13.mapPartitions(process).collect())  # 函数：list传入 list返回


    # foreachPartition：依次处理的是一整个分区  (foreach是一条数据地处理)  【性能加强】
    rdd14 = sc.parallelize([3, 2, 6, 893, 23, 22], 3)
    def process(iter):
        result = list()
        for it in iter:
            result.append(it * 10)
        print(result)
    rdd14.foreachPartition(process)  # 返回值是None


    # partitionBy：对rdd自定义分区操作  参数(重新定义几个分区、自定义分区规则)
    rdd15 = sc.parallelize([('hadoop', 1), ('spark', 1), ('hello', 1), ('flink', 1), ('spark', 1), ('hadoop', 1)])
    def process(key):
        if 'hadoop' == key: return 0
        if ('spark' == key) or ('flink' == key): return 1
        return 2
    print(rdd15.partitionBy(3, process).glom().collect())  # 函数：接受一个参数、返回分区号


    # repartition：对rdd分区执行重新分区 (仅在数量)  【慎重使用：会影响并行计算、极大可能导致shuffle】
    rdd16 = sc.parallelize([3, 2, 6, 893, 23, 22], 3)
    print(rdd16.repartition(5).glom().collect())


    # coalesce：对分区数增减  参数(分区数、tf是否允许shuffle 默认f不能增加分区只能减分区)
    rdd17 = sc.parallelize([3, 2, 6, 893, 23, 22], 3)
    print(rdd17.glom().collect())  # [[3, 2], [6, 893], [23, 22]]
    print(rdd17.coalesce(5).glom().collect())  # [[3, 2], [6, 893], [23, 22]]
    print(rdd17.coalesce(5, shuffle=True).glom().collect())  # [[], [], [], [], [3, 2, 6, 893, 23, 22]]
    print(rdd17.coalesce(2).glom().collect())  # [[3, 2], [6, 893, 23, 22]]


    # mapValues：针对kv型rdd，对v执行map
    rdd18 = sc.parallelize([('a', 1), ('E', 11), ('C', 4), ('D', 21), ('b', 122), ('g', 7), ('f', 3)])
    print(rdd18.map(lambda x: (x[0], x[1] * 10)).collect())
    print(rdd18.mapValues(lambda x: x * 10).collect())
