# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 8:44
# @File    ：demo7_AToperatorRDD.py
# @Function:

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('AToperatorRDD')
    sc = SparkContext(conf=conf)

    # countByKey：针对kv型rdd，统计k出现次数
    rdd1 = sc.textFile('../data/input/words.txt')
    print(rdd1.flatMap(lambda x:x.split(' ')).map(lambda x: (x,1)).countByKey())  # 结果是dict 不是rdd

    # collect：将rdd各个分区的数据，统一收集到Driver中，形成list对象 (收集数据不要太大 否则会把Driver内存撑爆)

    # ruduce：对rdd按照自定义规则进行聚合
    print(sc.parallelize(range(1, 10)).reduce(lambda a, b: a + b))  # 对rdd数据累加求和
    # fold：带有初始值的聚合
    print(sc.parallelize(range(1, 10), 3).fold(10, lambda a, b: a + b))  # +10*3(分区内聚合) +10(分区间聚合)


    # first：取出rdd的第一个元素
    print(sc.parallelize([3, 2, 1]).first())
    # taken：取出rdd前n个元素，返回成list
    print(sc.parallelize([3, 2, 6, 893, 23, 22]).take(3))  # [3, 2, 6]
    # top：对rdd降序排序，取前n个
    print(sc.parallelize([3, 2, 6, 893, 23, 22]).top(3))  # [893, 23, 22]
    # count：计算rdd有多少条数据，返回值是一个数字
    print(sc.parallelize([3, 2, 6, 893, 23, 22]).count())  # 6
    # takeSample：随机抽样rdd的数据  参数(tf是否重复同一位置、抽几个、随机种子)
    print(sc.parallelize([3, 2, 6, 893, 23, 22]).takeSample(True, 5))  # [893, 6, 893, 893, 2]
    print(sc.parallelize([3, 2, 6, 893, 23, 22]).takeSample(False, 5))
    # takeOrdered：对rdd自然升序取前n个  参数(要几个、对排序数据进行更改)
    print(sc.parallelize([3, 2, 6, 893, 23, 22], 1).takeOrdered(3))  # [2, 3, 6]
    print(sc.parallelize([3, 2, 6, 893, 23, 22], 1).takeOrdered(3, lambda x: -x))  # [893, 23, 22] 倒序


    # foreach：对rdd每个元素执行自定义逻辑 (与map一样  但没有返回值None)  【分布式执行 不经过Driver 直接写出】
    rdd11 = sc.parallelize([3, 2, 6, 893, 23, 22], 1)
    rdd11_1 = rdd11.foreach(lambda x: print(x * 10))
    print(rdd11_1)

    # saveAsTextFile：将rdd数据写入文本文件中  (本地路径 hdfs)  【分布式执行 不经过Driver 直接写出】
    rdd12 = sc.parallelize([3, 2, 6, 893, 23, 22], 1)
    rdd12.saveAsTextFile('../data/output/22')
    # rdd12.saveAsTextFile('hdfs://node1:8020/test/input/11111')
