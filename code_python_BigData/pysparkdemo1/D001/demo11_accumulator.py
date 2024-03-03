# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/8 23:09
# @File    ：demo11_accumulator.py
# @Function: 没有使用累加器

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('accumulator').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
    acmlt = 0


    def map_func(data):
        global acmlt
        count += 1
        print(count)


    rdd.map(map_func).collect()
    print(acmlt)

    """
    1 2 3 4 5 
    1 2 3 4 5 
    0
    """
