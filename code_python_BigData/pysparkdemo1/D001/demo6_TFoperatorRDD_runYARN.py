# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 8:08
# @File    ：demo6_TFoperatorRDD_runYARN.py
# @Function:

import os
import json
from pyspark import SparkConf, SparkContext

os.environ['HADOOP_CONF_DIR'] = '/export/server/hadoop/etc/hadoop'  # cd /export/server/spark/conf/; vim spark-env.sh

if __name__ == '__main__':
    conf = SparkConf().setAppName('orderRDD-runYARN').setMaster('yarn')  # yarn
    sc = SparkContext(conf=conf)

    rdd_file = sc.textFile('hdfs://node1:8020/test/input/order.text')  # hdfs
    rdd_result = rdd_file.flatMap(lambda line: line.split('|')).map(lambda x: json.loads(x)) \
        .filter(lambda x: x['areaName'] == '北京').map(lambda x: (x['areaName'], x['category'])).distinct()
    print(rdd_result.collect())
