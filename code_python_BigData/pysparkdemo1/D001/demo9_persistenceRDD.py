# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 11:14
# @File    ：demo9_persistenceRDD.py
# @Function:

from pyspark import SparkConf, SparkContext
from pyspark.storagelevel import StorageLevel

if __name__ == '__main__':
    conf = SparkConf().setAppName('persistenceRDD')
    sc = SparkContext(conf=conf)

    rdd3 = sc.parallelize([3, 2, 6, 893, 23, 22], 3)

    rdd3.cache()  # 缓存到内存中
    rdd3.persist(StorageLevel.MEMORY_ONLY)  # 仅内存缓存
    rdd3.persist(StorageLevel.MEMORY_ONLY_2)  # 仅内存缓存 2个副本
    rdd3.persist(StorageLevel.DISK_ONLY)  # 仅缓存硬盘上
    rdd3.persist(StorageLevel.DISK_ONLY_2)  # 仅缓存硬盘上 2个副本
    rdd3.persist(StorageLevel.DISK_ONLY_3)  # 仅缓存硬盘上 3个副本
    rdd3.persist(StorageLevel.MEMORY_AND_DISK)  # 先方内存 不够方硬盘 【推荐】
    rdd3.persist(StorageLevel.MEMORY_AND_DISK_2)  # 先方内存 不够方硬盘 2个副本
    rdd3.persist(StorageLevel.OFF_HEAP)  # 堆外内存(系统内存)

    rdd3.unpersist()  # 主动清理缓存
