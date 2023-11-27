# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 10:46
# @File    ：item.py
# @Function:

import datetime

import datetime


class Item:
    def __init__(self, description, duration):
        self.timestamp = datetime.datetime.now()
        self.description = description
        self.duration = duration

    def get_attributes(self):
        return {
            'Timestamp': self.timestamp,
            'Description': self.description,
            'Duration': self.duration
        }
