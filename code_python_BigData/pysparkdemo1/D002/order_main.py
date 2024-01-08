# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 8:17
# @File    ：order_main.py
# @Function:

import os
import json
from pyspark import SparkConf, SparkContext
from defs import city_with_category  # ModuleNotFoundError: No module named 'defs'

os.environ['HADOOP_CONF_DIR'] = '/export/server/hadoop/etc/hadoop'

if __name__ == '__main__':
    conf = SparkConf().setAppName('orderRDD-runYARN').setMaster('yarn')
    conf.set('spark.submit.pyFiles', 'defs.py') # 依赖文件同步上传到集群中 (可以是单个py文件 也可以是.zip压缩包)
    sc = SparkContext(conf=conf)

    rdd_file = sc.textFile('hdfs://node1:8020/test/input/order.text')
    rdd_result = rdd_file.flatMap(lambda line: line.split('|')).map(lambda x: json.loads(x)) \
        .filter(lambda x: x['areaName'] == '北京').map(city_with_category).distinct()
    print(rdd_result.collect())