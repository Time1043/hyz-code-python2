# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/15 13:27
# @File    ：wx.py
# @Function:

import requests

url = 'https://mp.weixin.qq.com/s/fvDsf2VNAxAb1cPx85RLww'
resp = requests.get(url=url)
print(resp)