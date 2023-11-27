# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/10 21:16
# @File    ：case11-baidu1.py
# @Function:
# import json多引用了,就当调试了
import urllib
import requests
import re

realkeyword = input('请输入要下载的图片的主题:')
keyword = urllib.parse.quote(realkeyword)
# url = 'https://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1589534417282_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%A3%AE%E6%9E%97'
# url1 = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1589534417282_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E6%A3%AE%E6%9E%97'
preurl = 'https://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1589534417282_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word='
# 想知道为什么上面有两个长得差不多的url吗?因为我把flip写成了index,所以一直find.all里面永远是空的,草了,让我找了一整天,熬了俩天夜
url = preurl + keyword
# print(url)
# print(url1)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
response = requests.get(url, headers=headers).text
# print(response)
pic_urls = re.findall('"hoverURL":"(.*?)",', response, re.S)
# for pic_url in pic_urls
# print(pic_urls)
# 千呼万唤始出来,终于来了
# img_url=[]
# try:	#多用用try，防止加载失败，程序退出
#    result=json.loads(res)
#    if result:
#        for i in result.get("data"):
#            img_url.append(i.get("hoverURL"))
# except:
#    print("获取图片地址失败")
#
# print(result)
# response.status_code
# print(response.status_code)200
# 我还以为是re正规表达式错了,专门学了学json,妈的

# 不是objURL,因为我懒得解密了
for i, pic_url in enumerate(pic_urls):
    try:
        pic = requests.get(pic_url, headers=headers, timeout=15)
        name = str(i + 1) + '.jpg'
        with open(name, 'wb') as f:
            f.write(pic.content)
            print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
    except Exception as e:
        print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
        continue
