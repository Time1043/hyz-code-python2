# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/22 11:22
# @File    ：demo2.py
# @Function:

import pdfplumber

path = r"C:\Users\huangyingzhu\Desktop\Transformer\1412.7449_Grammar as a Foreign Language.pdf"
with pdfplumber.open(path) as pdf:
    for page in pdf.pages:
        for form in page.extract_text():
            print(form)
