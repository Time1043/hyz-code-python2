# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 15:20
# @File    ：log_main.py
# @Function:

from pyspark import SparkConf, SparkContext
from pyspark.storagelevel import StorageLevel
from defs import context_jieba, filter_words, append_words
from defs import extract_user_word
from operator import add

if __name__ == '__main__':
    conf = SparkConf().setAppName('log-main').setMaster('local[*]')  # 本地运行
    sc = SparkContext(conf=conf)

    rdd_file = sc.textFile('../data/input/SogouQ.txt')
    rdd_line = rdd_file.map(lambda x: x.split('\t'))
    rdd_line.persist(StorageLevel.DISK_ONLY)  # 多次使用 持久化
    print(rdd_line.takeSample(True, 3))  # [['09:00:17', '15984948747597305', '传智汇', '2', '4', 'http://www.itcast.cn'],

    # 需求1：用户搜索关键词分析
    rdd_context1 = rdd_line.map(lambda x: x[2])
    # print(rdd_context1.takeSample(True, 3))  # ['scala', 'hadoop', '数据仓库']
    rdd_words1 = rdd_context1.flatMap(context_jieba)
    # print(rdd_words1.collect())
    rdd_edit1 = rdd_words1.filter(filter_words).map(append_words)  # 手动修改
    # print(rdd_edit1.collect())
    rdd_result1 = rdd_edit1.reduceByKey(lambda a, b: a + b).sortBy(lambda x:x[1], ascending=False, numPartitions=1)
    print(rdd_result1.take(5))

    # 需求2：用户和关键词组合分析
    rdd_user_word2 = rdd_line.map(lambda x: (x[1], x[2]))
    # print(rdd_user_word.takeSample(True, 3))  # [('4597407597846744', 'bigdata'),
    rdd_edit2 = rdd_user_word2.flatMap(extract_user_word)
    # print(rdd_edit2.collect())  # [('2982199073774412_传智播客', 1),
    rdd_result2 = rdd_edit2.reduceByKey(lambda a, b: a + b).sortBy(lambda x: x[1], ascending=False, numPartitions=1)
    print(rdd_result2.collect())

    # 需求3：热门搜索时间段分析
    rdd_time3 = rdd_line.map(lambda x: x[0])  # ['20:00:07', '20:00:07',
    rdd_hour3 = rdd_time3.map(lambda x: (x.split(':')[0], 1))  # [('23', 1), ('12', 1), ('21', 1),
    rdd_result3 = rdd_hour3.reduceByKey(add).sortBy(lambda x: x[1], ascending=False, numPartitions=1)  # 分组聚合 排序
    print(rdd_result3.collect())
