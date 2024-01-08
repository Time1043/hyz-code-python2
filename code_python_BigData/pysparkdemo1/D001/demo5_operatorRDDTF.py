# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/7 20:51
# @File    ：demo5_operatorRDDTF.py
# @Function:

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('operatorRDD2').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    # groupBy：将rdd数据进行分组  hash分组
    rdd1 = sc.parallelize([('a', 1), ('b', 1), ('a', 1), ('a', 1), ('b', 1), ])
    print(rdd1.groupBy(lambda x: x[0]).collect())  # [('b', <object>), ('a', <object>)]
    print(rdd1.groupBy(lambda x: x[0]).map(lambda x:(x[0], list(x[1]))).collect())  # [('b', [('b', 1), ('b', 1)]), ('a', [('a', 1), ('a', 1), ('a', 1)])]

    rdd1 = sc.parallelize([1, 2, 3, 4, 5])
    rdd1_eo = rdd1.groupBy(lambda num: 'even' if (num % 2 == 0) else 'odd')  # 偶数奇数
    print(rdd1_eo.map(lambda x: (x[0], list(x[1]))).collect())  # [('even', [2, 4]), ('odd', [1, 3, 5])]

    # filter：过滤想要的数据进行保留 (返回值为true的数据保留)
    rdd2 = sc.parallelize([1, 2, 3, 4, 5])
    print(rdd2.filter(lambda x: x % 2 == 1).collect())  # 保留奇数

    # distinct：对rdd数据进行去重
    rdd3 = sc.parallelize([1, 1, 2, 2, 2, 5, 6, 6, 6, 9])
    print(rdd3.distinct().collect())

    rdd3 = sc.textFile('../data/input/words.txt')
    print(rdd3.collect())
    print(rdd3.flatMap(lambda line: line.split(' ')).collect())  # 按照空格切分数据 解除嵌套
    print(rdd3.flatMap(lambda line: line.split(' ')).distinct().collect())  # 去重

    # union：2个rdd合并成1个rdd (只合并不去重 允许不同类型)
    rdd4_1 = sc.parallelize([1, 1, 2, 3])
    rdd4_2 = sc.parallelize([2, 5, 5, 5, 6, 9, 9, 9])
    rdd4_union = rdd4_1.union(rdd4_2)
    print(rdd4_union.collect())

    # join：针对kv型rdd，对两个rdd按照k进行join (可实现sql内连接外连接)
    rdd5_1 = sc.parallelize([(1001, 'zhangsan'), (1001, 'lisi'), (1002, 'wangermazi'), (1002, 'zhaoliu'), (1005, 'qianqi')])
    rdd5_2 = sc.parallelize([(1001, 'sales'), (1002, 'tech'), (1006, 'dev')])
    print(rdd5_1.join(rdd5_2).collect())  # 内连接
    print(rdd5_1.leftOuterJoin(rdd5_2).collect())  # 左外连接
    print(rdd5_1.rightOuterJoin(rdd5_2).collect())  # 右外连接

    # intersection：求2个rdd的交集
    rdd6_1 = sc.parallelize([('a', 1), ('b', 1)])
    rdd6_2 = sc.parallelize([('a', 1), ('c', 1)])
    print(rdd6_1.intersection(rdd6_2).collect())

    # glom：加上嵌套，分区 (能够看到分区排布)
    rdd7 = sc.parallelize([1, 2, 3, 4, 5], 3)
    print(rdd7.glom().collect())  # [[1], [2, 3], [4, 5]]
    print(rdd7.glom().flatMap(lambda x: x).collect())  # 解嵌套 传空实现 (要flat不map)  [1, 2, 3, 4, 5]

    # groupByKey：针对kv型rdd，自动按照k分组
    rdd8 = sc.parallelize([('a', 1), ('a', 1), ('b', 1), ('b', 1), ('b', 1)])
    print(rdd8.groupByKey().collect())  # [('b', <object>), ('a', <object>)]
    print(rdd8.groupByKey().map(lambda x: (x[0], list(x[1]))).collect())  # [('b', [1, 1, 1]), ('a', [1, 1])]

    # sortBy：按照指定规则排序
    rdd9 = sc.parallelize([('a', 1), ('c', 6), ('a', 6), ('b', 6), ('c', 6), ('b', 1), ('b', 5), ('b', 11)])
    print(rdd9.sortBy(lambda x: x[1], ascending=True, numPartitions=3).collect())  # 参数：规则、升序、分区数 (若想保证全局有序 分区数为1)
    print(rdd9.sortBy(lambda x: x[0], ascending=False, numPartitions=3).collect())

    # sortByKey：针对kv型rdd，按照k进行排序
    rdd10 = sc.parallelize([('a', 1), ('E', 1), ('C', 1), ('D', 1), ('b', 1), ('g', 1), ('f', 1),
                            ('y', 1), ('u', 1), ('i', 1), ('o', 1), ('p', 1), ('z', 1), ('w', 1),
                            ('m', 1), ('n', 1), ('j', 1), ('k', 1), ('l', 1), ('Q', 1)], 2)
    print(rdd10.glom().collect())
    print(rdd10.sortByKey().collect())
    print(rdd10.sortByKey(ascending=False, numPartitions=5).collect())  # (若想保证全局有序 分区数为1)
    print(rdd10.sortByKey(ascending=True, numPartitions=1, keyfunc=lambda key: str(key).lower()).collect())  # 排序前先处理keyfunc

