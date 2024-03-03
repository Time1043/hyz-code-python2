# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 7:43
# @File    ：demo6_operatorRDDTF_run.py
# @Function:

import json
from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('orderRDD')
    sc = SparkContext(conf=conf)

    rdd_file = sc.textFile('../data/input/order.text')
    rdd_result = rdd_file.flatMap(lambda line: line.split('|')).map(lambda x: json.loads(x)) \
        .filter(lambda x: x['areaName'] == '北京').map(lambda x: (x['areaName'], x['category'])).distinct()
    print(rdd_result.collect())
