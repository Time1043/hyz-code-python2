# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/2 7:59
# @File    ：demo2.py
# @Function:


keywords = ['ipad']
base_url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.6.2&appKey=12574478&api=mtop.relationrecommend.WirelessRecommend.recommend&v=2.0&type=jsonp&dataType=jsonp&"

for keyword in keywords:
    for page in range(20):  # 这里 range(2) 只会产生 0 和 1，如果你想要第 1 页和第 2 页，则需要 range(1, 3)
        callback_value = f"mtopjsonp{page + 1}"
        data_value = f'%7B%22appId%22%3A%2234385%22%2C...%2C%5C%22page%5C%22%3A{page}%2C...%2C%5C%22q%5C%22%3A%5C%22{keyword}%5C%22%2C...%7D'
        # 在上述 data_value 中，我使用了 ... 作为其他参数的占位符，你需要替换这部分为实际的其他参数。

        url = f'{base_url}callback={callback_value}&data={data_value}'
        print(url)  # 你可以先打印 URL 来检查它是否正确
        # yield scrapy.Request(url=url, callback=self.parse)  # 如果你使用 Scrapy，你可能需要像这样发送请求

