# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/7 20:14
# @File    ：demo4_TFoperatorRDD.py
# @Function:

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    def map_func(data):
        return data * 10


    conf = SparkConf().setAppName('operatorRDD').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # map：执行自定义的函数逻辑
    rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6], 3)
    print(rdd1.map(map_func).collect())  # 高阶函数 复杂逻辑
    print(rdd1.map(lambda data: data * 10).collect())  # 匿名函数

    # flatMap：先map、在解除嵌套
    rdd2 = sc.parallelize(['hdfs hadoop mapreduce', 'yarn spark mapreduce', 'kafka flink mapreduce'])
    print(rdd2.map(lambda line: line.split(' ')).collect())  # 嵌套的 [[],[],[]]
    print(rdd2.flatMap(lambda line: line.split(' ')).collect())  # 解除嵌套 [,,,,,,]

    # reduceByKey：针对kv型rdd，先按k分组(ByKey)、再自定义逻辑完成组内数据v的聚合(reduce) - 要求类型一致 f(V,V)->V
    rdd3 = sc.parallelize([('hadoop', 1), ('spark', 1), ('hadoop', 5), ('flink', 1), ('flink', 1)])
    print(rdd3.reduceByKey(lambda a, b: a + b).collect())  # 两两的聚合逻辑 迭代ab

    # mapValues：针对kv型rdd，对v执行map
    rdd4 = sc.parallelize([('hadoop', 1), ('spark', 1), ('hadoop', 5), ('flink', 1), ('flink', 1)])
    print(rdd4.map(lambda x: (x[0], x[1] * 10)).collect())
    print(rdd4.mapValues(lambda x: x * 10).collect())
