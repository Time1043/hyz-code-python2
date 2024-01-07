# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/7 20:51
# @File    ：demo5_operatorRDD.py
# @Function:

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('operatorRDD2').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # # groupBy：将rdd数据进行分组
    # rdd1 = sc.parallelize([1, 2, 3, 4, 5])
    # rdd1_eo = rdd1.groupBy(lambda num: 'even' if (num % 2 == 0) else 'odd')  # 偶数奇数
    # print(rdd1_eo.map(lambda x: (x[0], list(x[1]))).collect())
    #
    # # filter：过滤想要的数据进行保留
    # rdd2 = sc.parallelize([1, 2, 3, 4, 5])
    # print(rdd2.filter(lambda x: x % 2 == 1).collect())  # 保留奇数
    #
    # # distinct：对rdd数据进行去重
    # rdd3 = sc.parallelize([1, 1, 2, 2, 2, 5, 6, 6, 6, 9])
    # print(rdd3.distinct().collect())
    #
    # rdd3 = sc.textFile('../data/input/words.txt')
    # print(rdd3.collect())
    # print(rdd3.flatMap(lambda line: line.split(' ')).collect())  # 按照空格切分数据 解除嵌套
    # print(rdd3.flatMap(lambda line: line.split(' ')).distinct().collect())  # 去重
    #
    # # union：2个rdd合并成1个rdd (只合并 不去重)
    # rdd4_1 = sc.parallelize([1, 1, 2, 3])
    # rdd4_2 = sc.parallelize([2, 5, 5, 5, 6, 9, 9, 9])
    # rdd4_union = rdd4_1.union(rdd4_2)
    # print(rdd4_union.collect())
    #
    # # join：针对kv型rdd，对两个rdd进行join (可实现sql内连接外连接)
    # rdd5_1 = sc.parallelize([(1001, 'zhangsan'), (1001, 'lisi'), (1002, 'wangermazi'), (1002, 'zhaoliu'), (1005, 'qianqi')])
    # rdd5_2 = sc.parallelize([(1001, 'sales'), (1002, 'tech'), (1006, 'dev')])
    # print(rdd5_1.join(rdd5_2).collect())  # 内连接
    # print(rdd5_1.leftOuterJoin(rdd5_2).collect())  # 左外连接
    # print(rdd5_1.rightOuterJoin(rdd5_2).collect())  # 右外连接
    #
    # # intersection：求2个rdd的交集
    # rdd6_1 = sc.parallelize([('a', 1), ('b', 1)])
    # rdd6_2 = sc.parallelize([('a', 1), ('c', 1)])
    # print(rdd6_1.intersection(rdd6_2).collect())
    #
    # # glom：加上嵌套，分区
    # rdd7 = sc.parallelize([1, 2, 3, 4, 5], 3)
    # print(rdd7.glom().collect())
    #
    # # groupByKey：针对kv型rdd，自动按照k分组
    # rdd8 = sc.parallelize([('a', 1), ('a', 1), ('b', 1), ('b', 1), ('b', 1)])
    # print(rdd8.groupByKey().collect())
    # print(rdd8.groupByKey().map(lambda x: (x[0], list(x[1]))).collect())  # [('b', [1, 1, 1]), ('a', [1, 1])]

    # sortBy：按照指定规则排序


    # sortByKey：针对kv型rdd，按照k进行排序

