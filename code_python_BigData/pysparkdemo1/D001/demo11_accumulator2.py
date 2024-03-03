# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/8 23:09
# @File    ：demo11_accumulator2.py
# @Function: 没有使用累加器

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('accumulator').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    acmlt = sc.accumulator(0)  # 累加器变量 参数是初始值


    def map_func(data):
        global acmlt
        acmlt += 1
        print(acmlt)


    rdd2 = rdd.map(map_func)
    rdd2.cache()  # 用缓存避免
    rdd2.collect()

    rdd3 = rdd2.map(lambda x: x)
    rdd3.collect()

    print(acmlt)

    """
    1 2 3 4 5 
    1 2 3 4 5 
    10 
    """
