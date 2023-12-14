# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/14 20:37
# @File    ：demo6DouYin.py
# @Function: 下载视频

import requests

resp = requests.get(
    url='https://v3-web.douyinvod.com/456ede467097556b83dce0b24f18c37c/657b062b/video/tos/cn/tos-cn-ve-15c001-alinc2/o0EzkfQFmXyBABu3cWFAAChAhPNb4UYIngtf9J/?a=6383&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1450&bt=1450&cs=0&ds=6&ft=bvTKJbQQqUGXf_.ZWo0ORVTYA0piSzdTejKJNjLWGG0P3-I&mime_type=video_mp4&qs=0&rc=aWg8N2hmZmk6aGY4ZWg2NkBpM252czg6ZnM1bTMzNGkzM0BfLy1hM2IyXjIxLmI1M19jYSNrMW5vcjRfMnBgLS1kLWFzcw%3D%3D&btag=e00028000&dy_q=1702557585&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=202312142039458B02CC70825B8C090A0A'
)
print(resp.content)

with open('v2.mp4', mode='wb') as f:
    f.write(resp.content)
