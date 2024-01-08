# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/8 15:09
# @File    ：demo1.py
# @Function:

import jieba

if __name__ == '__main__':
    content = '幸福的家庭都是相似的，不幸的家庭各有各的不幸。列夫托尔斯泰说的'

    result = jieba.cut(content, True)
    print(type(result))  # <class 'generator'>
    print(result)  # <generator object Tokenizer.cut at 0x7f9ab7fa2430>
    print(list(result))  # ['幸福', '的', '家庭', '都', '是', '相似', '似的', '，', '不幸', '的', '家庭', '各', '有', '各', '的', '不幸', '。', '列', '夫', '托尔', '托尔斯', '托尔斯泰', '尔斯', '泰', '说', '的']

    # 搜索引擎场景
    result2 = jieba.cut_for_search(content)
    print(', '.join(result2))
