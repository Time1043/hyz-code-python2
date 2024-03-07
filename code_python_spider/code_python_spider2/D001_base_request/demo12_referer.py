# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/3/3 15:17
# @File    ：demo12_referer.py
# @Function:

import requests


def req_pearvideo():
    url = 'https://pearvideo.com/videoStatus.jsp?contId=1792192&mrd=0.06856278007630534'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://pearvideo.com/video_1792192',
    }

    resp = requests.get(url=url, headers=headers)
    # print(resp.text)  # 验证成功

    resp_json = resp.json()
    url_mp4 = resp_json['videoInfo']['videos']['srcUrl']
    print(url_mp4)  # 验证成功
    # https://video.pearvideo.com/mp4/short/20240228/1709450870279-71105833-hd.mp4  req
    # https://video.pearvideo.com/mp4/short/20240224/cont-1792192-16020138-hd.mp4  html

    system_time = resp_json['systemTime']
    url_mp4_real = url_mp4.replace(system_time, 'cont-1792192')
    print(url_mp4_real)  # 验证成功

    resp_mp4 = requests.get(url=url_mp4_real)
    with open('demo1.mp4', 'wb') as f:
        f.write(resp_mp4.content)


if __name__ == '__main__':
    print('start...')

    req_pearvideo()

    print('end...')
