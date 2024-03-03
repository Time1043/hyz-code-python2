# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/8 22:26
# @File    ：demo10_broadcast.py
# @Function: 没有使用广播变量的

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('broadcast').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    stu_info_list = [(1, '张三', 11), (2, '李四', 13), (3, '王二麻子', 11), (4, '赵六', 11), ]
    score_info_rdd = sc.parallelize([(1, '语文', 99), (2, '数学', 99), (3, '英语', 99), (4, '编程', 99),
                                     (1, '语文', 99), (2, '编程', 99), (3, '语文', 99), (4, '英语', 99),
                                     (1, '语文', 99), (3, '英语', 99), (2, '编程', 99), ])


    def map_func(data):  # data为score_info_rdd
        id = data[0]
        name = ''
        for stu_info in stu_info_list:
            stu_id = stu_info[0]
            if id == stu_id:  # 匹配成功
                name = stu_info[1]
        return (name, data[1], data[2])


    print(score_info_rdd.map(map_func).collect())
