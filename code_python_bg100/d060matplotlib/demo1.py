# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/7 14:40
# @File    ：demo1.py
# @Function:

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.4, 1.4, 30)
plt.plot(x, x ** 2)
plt.savefig('demo1.png')
plt.show()
