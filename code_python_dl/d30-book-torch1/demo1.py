# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/23 19:48
# @File    ：demo1.py
# @Function: 简单认识张量

import torch

print(torch.version.__version__)  # 查看torch版本2.1.0

# torch基本的数据格式：张量tensor
a = torch.ones(3, 3)
b = torch.ones(3, 3)
print(a)
print(a + b)

# 是否显卡被激活
print(torch.cuda.is_available())  # True

# 放到gpu中
a = a.to('cuda')
# print(a + b)  # RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!
b = b.to('cuda')
print(a + b)  # device='cuda:0'
