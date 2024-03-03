# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 15:36
# @File    ：defs.py
# @Function:

import jieba


def context_jieba(data):
    """ 通过jieba分词工具，进行中文分词处理 """
    seg = jieba.cut_for_search(data)
    l = list()
    for word in seg:
        l.append(word)
    return l


def filter_words(data):
    """ 过滤不要的词 """
    return data not in ['谷', '帮', '客']


def append_words(data):
    """ 修订某些关键词  为了后面的单词计数 """
    if data == '传智播': return ('传智播客', 1)
    if data == '院校': return ('院校帮', 1)
    if data == '博学': return ('博学谷', 1)
    return (data, 1)


def extract_user_word(data):
    """ 传入数据是一个元组 """
    user_id = data[0]
    content = data[1]

    words = context_jieba(content)
    return_list = list()
    for word in words:
        if filter_words(word):
            return_list.append((user_id + '_' + append_words(word)[0], 1))

    return return_list
