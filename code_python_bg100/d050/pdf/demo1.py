# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/22 11:03
# @File    ：demo1.py
# @Function:

import pdfplumber

path = r"C:\Users\huangyingzhu\Desktop\Transformer\1412.7449_Grammar as a Foreign Language.pdf"
with pdfplumber.open(path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()  # 对指定页提取文本
        text += '\n\n\n'
        file = open(r'C:\Users\huangyingzhu\Desktop\1.txt', mode='a', encoding='utf-8')
        file.write(text)
