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


class Request(object):
    def __init__(self, req, xx):
        self._request = req
        self.xx = xx

    def __getattr__(self, attr):  # attr='yyy'
        try:
            return getattr(self._request, attr)  # 反射 self._request.yyy => req.yyy
        except AttributeError:
            return self.__getattribute__(attr)


req = HttpRequest()
req.method()
req.path_info()

request = Request(req, 11)
print(request.xx)
print(request._request)
request._request.method()
request._request.path_info()
