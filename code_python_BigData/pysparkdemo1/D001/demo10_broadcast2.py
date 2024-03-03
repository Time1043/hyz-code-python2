# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/8 22:26
# @File    ：demo10_broadcast2.py
# @Function: 使用广播变量的

from pyspark import SparkConf, SparkContext

if __name__ == '__main__':
    conf = SparkConf().setAppName('broadcast').setMaster('local[*]')
    sc = SparkContext(conf=conf)

    stu_info_list = [(1, '张三', 11), (2, '李四', 13), (3, '王二麻子', 11), (4, '赵六', 11), ]
    score_info_rdd = sc.parallelize([(1, '语文', 99), (2, '数学', 99), (3, '英语', 99), (4, '编程', 99),
                                     (1, '语文', 99), (2, '编程', 99), (3, '语文', 99), (4, '英语', 99),
                                     (1, '语文', 99), (3, '英语', 99), (2, '编程', 99), ])
    broadcast = sc.broadcast(stu_info_list)  # 将本地list标记为广播变量


    def map_func(data):
        id = data[0]
        name = ''
        for stu_info in broadcast.value:  # 使用广播变量
            stu_id = stu_info[0]
            if id == stu_id:
                name = stu_info[1]
        return (name, data[1], data[2])


    print(score_info_rdd.map(map_func).collect())
