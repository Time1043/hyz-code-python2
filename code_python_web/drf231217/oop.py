# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/17 18:12
# @File    ：oop.py
# @Function:

class HttpRequest(object):
    def __init__(self):
        pass

    def method(self):
        print('django的method')

    def path_info(self):
        print('django的path_info')


class DrfRequest(object):
    def __init__(self, req, xx):
        self._request = req
        self.xx = xx

    def __getattr__(self, attr):  # attr='yyy'
        try:
            return getattr(self._request, attr)  # 反射 self._request.yyy => req.yyy
        except AttributeError:
            return self.__getattribute__(attr)


req = HttpRequest()  # django
req.method()
req.path_info()

request = DrfRequest(req, 11)  # drf
print(request)  # drf的request
print(request._request)  # django的request
request._request.method()
request._request.path_info()

print(request.method())  # drf没有method成员 就去django中找
print(request.path_info())  # drf没有method成员 就去django中找
