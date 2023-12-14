# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 21:19
# @File    ：demo5YiChe.py
# @Function:

import requests
from bs4 import BeautifulSoup

url1 = "https://mapi.yiche.com/web_api/car_model_api/api/v1/master/search_hot_masters?cid=508&param=%7B%22type%22%3A2%2C%22adCigdcid%22%3A%22kiycJaaF3teETzRTNtCyDWhkm6YMAcdG%26page%3D7SnwJ7pTDYesxnmNa5hRDSebfrDXeTkj1702559585696%22%2C%22adTime%22%3A%222023-12-14%22%2C%22advertPage%22%3A%227SnwJ7pTDYesxnmNa5hRDSebfrDXeTkj1702559585696%22%7D"
headers1 = {
    "Content-Type": "application/json;charset=utf-8",
    'Cookie': "isWebP=true; locatecity=350600; bitauto_ipregion=112.109.248.83%3A%E7%A6%8F%E5%BB%BA%E7%9C%81%E6%BC%B3%E5%B7%9E%E5%B8%82%3B305%2C%E6%BC%B3%E5%B7%9E%E5%B8%82%2Czhangzhou; CIGUID=eeac5a4a-f3d2-4d75-aa4c-b37cdfab020e; auto_id=db091de5f7b730eaa6e86bc725722415; CIGDCID=kiycJaaF3teETzRTNtCyDWhkm6YMAcdG; UserGuid=eeac5a4a-f3d2-4d75-aa4c-b37cdfab020e; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1702559569; selectcity=350600; selectcityid=305; selectcityName=%E6%BC%B3%E5%B7%9E; Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1702559586",
    'Referer': "https://car.yiche.com/",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
resp1 = requests.get(url=url1, headers=headers1)
print(resp1.json())

url2 = "https://mapi.yiche.com/web_api/car_model_api/api/v1/serial/search_hot_serials?cid=508&param=%7B%22adCigdcid%22%3A%22kiycJaaF3teETzRTNtCyDWhkm6YMAcdG%26page%3D7SnwJ7pTDYesxnmNa5hRDSebfrDXeTkj1702559585696%22%2C%22type%22%3A5%2C%22adTime%22%3A%222023-12-14%22%2C%22advertPage%22%3A%227SnwJ7pTDYesxnmNa5hRDSebfrDXeTkj1702559585696%22%2C%22num%22%3A20%7D"
headers1 = {
    "Content-Type": "application/json;charset=utf-8",
    'Cookie': "isWebP=true; locatecity=350600; bitauto_ipregion=112.109.248.83%3A%E7%A6%8F%E5%BB%BA%E7%9C%81%E6%BC%B3%E5%B7%9E%E5%B8%82%3B305%2C%E6%BC%B3%E5%B7%9E%E5%B8%82%2Czhangzhou; CIGUID=eeac5a4a-f3d2-4d75-aa4c-b37cdfab020e; auto_id=db091de5f7b730eaa6e86bc725722415; CIGDCID=kiycJaaF3teETzRTNtCyDWhkm6YMAcdG; UserGuid=eeac5a4a-f3d2-4d75-aa4c-b37cdfab020e; Hm_lvt_610fee5a506c80c9e1a46aa9a2de2e44=1702559569; selectcity=350600; selectcityid=305; selectcityName=%E6%BC%B3%E5%B7%9E; Hm_lpvt_610fee5a506c80c9e1a46aa9a2de2e44=1702559586",
    'Referer': "https://car.yiche.com/",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
resp2 = requests.get(url=url2)
