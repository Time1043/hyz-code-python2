# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/29 15:16
# @File    ：demo3_bilibili.py
# @Function:

import re
import os
import json
from pprint import pprint
import requests
import subprocess
import csv
import time
from datetime import datetime, timezone, timedelta


def video_already_downloaded(title, video_dir):
    # 检查目录中是否有以特定日期格式开头的同名视频
    pattern = re.compile(r'(?:【\d{6}】)?' + re.escape(title) + '.mp3')
    print('=====================================judge=====================================')
    for file in os.listdir(video_dir):
        if pattern.match(file):
            print('True')
            return True
    print('False')
    return False


def req_bilibili(bv):
    current_timestamp = time.time()
    local_time = datetime.fromtimestamp(current_timestamp)  # 将时间戳转换为datetime对象，这会自动转换为您系统的本地时间
    formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')  # 将datetime对象格式化为字符串
    print('=====================================req: download preparation=====================================')
    print(f'[TIME] {formatted_time}')

    url = f'https://www.bilibili.com/video/{bv}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://space.bilibili.com/299133172/video',
        'Cookie': "buvid3=4F077F14-7A50-826A-07B1-E13EA6AB4AF448919infoc; b_nut=1694935048; i-wanna-go-back=-1; b_ut=7; _uuid=3A4B9E6A-DFBE-227A-10B47-AC656EF10AD2550259infoc; buvid4=0BA435A9-694D-D159-6E04-3CC62C4D9FC749832-023091715-vEypQIU/lka2gSe0HRe/Lw%3D%3D; DedeUserID=259090980; DedeUserID__ckMd5=17f29169a9316ab9; rpdid=|(kJYJlklJJm0J'uYmRmJl|mk; header_theme_version=CLOSE; hit-dyn-v2=1; enable_web_push=DISABLE; fingerprint=01a4536074ecc0c3148b21a4dd20e781; buvid_fp_plain=undefined; buvid_fp=01a4536074ecc0c3148b21a4dd20e781; CURRENT_FNVAL=16; CURRENT_QUALITY=64; home_feed_column=5; browser_resolution=1400-747; bp_video_offset_259090980=889455871237554185; b_lsid=74761682_18D5414A9A6; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; SESSDATA=a59c52a9%2C1722064662%2Ca20d8%2A12CjCDSQfG0qvETz8_XBoZdCdnJwpmSU4TA3owoJURQm2GkhHpuvJHzsOK1nJop0KECgASVnlWZDU3ajQ4bGFjbjNid1EtSk5MYTdPSXE3TS1DRkRzX1lSMHZUYXh5UEZONkluR2dNclRhaXFLTk5BOWxYLWxjbllfWi12Skw0NEt4RHhHRGxVbVd3IIEC; bili_jct=411555cec512d063e9813df69d52cceb; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDY3NzE4ODAsImlhdCI6MTcwNjUxMjYyMCwicGx0IjotMX0.5pXjXz0mH2IyHrzpCqWLLg2zcK_FsfZS_lxif7qLcdk; bili_ticket_expires=1706771820; sid=8cn3j4k3; share_source_origin=copy_web; bsource=share_source_copylink_web; PVID=1"
    }

    resp = requests.get(url=url, headers=headers)
    resp_html = resp.text
    # print(resp_html)
    # with open('BLtest.html', 'w', encoding='utf-8') as f:
    #     f.write(resp_html)

    # 解析数据
    title = re.findall('<h1 title="(.*?)" class="video-title"', resp_html)[0].replace(' ', '_')
    # print(title)  # 验证成功
    video_info = re.findall('<script>window.__playinfo__=(.*?)</script>', resp_html)[0]
    # print(video_info)  # 验证成功
    json_data = json.loads(video_info)
    # pprint(json_data)  # 验证成功
    audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]  # 音频
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]  # 视频画面

    if not os.path.exists('./audio'):
        os.makedirs('./audio')
    if not os.path.exists('./video'):
        os.makedirs('./video')
    video_exists = video_already_downloaded(title, './audio')
    if video_exists:
        print('=====================================INFO=====================================')
        print(f"[INFO]  file {title} : exist, return... ...")
        return

    # # 定义音频和视频文件的路径
    # audio_path = os.path.join('audio', title + '.mp3')
    # video_path = os.path.join('video', title + '.mp4')
    # # 检查文件是否存在
    # audio_exists = os.path.exists(audio_path)
    # video_exists = os.path.exists(video_path)
    # # 检查文件如果是我本地存在的就跳过 否则就下载
    # if audio_exists:
    #     print(f"file {title} : exist, return... ...")
    #     return

    # if audio_exists and video_exists:
    #     print(f"file {title} : exist, return... ...")
    #     return
    # elif audio_exists or video_exists:
    #     # 删除已存在的文件
    #     if audio_exists:
    #         os.remove(audio_path)
    #         print(f"delete file: {audio_path}")
    #     if video_exists:
    #         os.remove(video_path)
    #         print(f"delete file: {video_path}")

    print('=====================================req: download=====================================')
    resp_audio = requests.get(url=audio_url, headers=headers).content
    resp_video = requests.get(url=video_url, headers=headers).content
    # if not os.path.exists('./audio'):
    #     os.makedirs('./audio')
    # if not os.path.exists('./video'):
    #     os.makedirs('./video')
    with open('audio\\' + title + '.mp3', mode='wb') as audio:
        audio.write(resp_audio)
    with open('video\\' + title + '.mp4', mode='wb') as video:
        video.write(resp_video)

    # 视频音频合并
    print('=====================================merge=====================================')
    if not os.path.exists('./data'):
        os.makedirs('./data')
    cmd = f"ffmpeg -loglevel error -i video\\{title}.mp4 -i audio\\{title}.mp3 -c:v copy -c:a aac -strict experimental data\\{title}.mp4"
    subprocess.run(cmd)


def req_bilibili_page():
    # url = 'https://api.bilibili.com/x/space/wbi/arc/search?mid=662609045&ps=30&tid=0&pn=1&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[%7B%22x%22:2932,%22y%22:-1511,%22z%22:0,%22timestamp%22:28538,%22k%22:70,%22type%22:0%7D,%7B%22x%22:3001,%22y%22:-1362,%22z%22:82,%22timestamp%22:28638,%22k%22:103,%22type%22:0%7D,%7B%22x%22:3055,%22y%22:-1301,%22z%22:138,%22timestamp%22:28739,%22k%22:106,%22type%22:0%7D,%7B%22x%22:3000,%22y%22:-1349,%22z%22:85,%22timestamp%22:28839,%22k%22:61,%22type%22:0%7D,%7B%22x%22:3143,%22y%22:-1185,%22z%22:234,%22timestamp%22:28943,%22k%22:83,%22type%22:0%7D,%7B%22x%22:2974,%22y%22:-1334,%22z%22:74,%22timestamp%22:29045,%22k%22:84,%22type%22:0%7D,%7B%22x%22:3166,%22y%22:-525,%22z%22:278,%22timestamp%22:29145,%22k%22:65,%22type%22:0%7D,%7B%22x%22:3284,%22y%22:598,%22z%22:348,%22timestamp%22:29246,%22k%22:70,%22type%22:0%7D,%7B%22x%22:2724,%22y%22:1021,%22z%22:59,%22timestamp%22:40125,%22k%22:62,%22type%22:0%7D,%7B%22x%22:3402,%22y%22:2001,%22z%22:889,%22timestamp%22:40227,%22k%22:84,%22type%22:0%7D,%7B%22x%22:3217,%22y%22:977,%22z%22:553,%22timestamp%22:40327,%22k%22:79,%22type%22:0%7D,%7B%22x%22:3673,%22y%22:-87,%22z%22:877,%22timestamp%22:40427,%22k%22:69,%22type%22:0%7D,%7B%22x%22:3077,%22y%22:-1080,%22z%22:230,%22timestamp%22:40529,%22k%22:101,%22type%22:0%7D,%7B%22x%22:2958,%22y%22:-1430,%22z%22:68,%22timestamp%22:40629,%22k%22:121,%22type%22:0%7D,%7B%22x%22:3610,%22y%22:-755,%22z%22:720,%22timestamp%22:40730,%22k%22:119,%22type%22:0%7D,%7B%22x%22:4485,%22y%22:230,%22z%22:1610,%22timestamp%22:40831,%22k%22:123,%22type%22:0%7D,%7B%22x%22:4220,%22y%22:-20,%22z%22:1346,%22timestamp%22:40932,%22k%22:63,%22type%22:0%7D,%7B%22x%22:4291,%22y%22:58,%22z%22:1419,%22timestamp%22:41033,%22k%22:75,%22type%22:0%7D,%7B%22x%22:3577,%22y%22:-655,%22z%22:702,%22timestamp%22:41140,%22k%22:108,%22type%22:0%7D,%7B%22x%22:4993,%22y%22:761,%22z%22:2118,%22timestamp%22:41248,%22k%22:120,%22type%22:0%7D,%7B%22x%22:3134,%22y%22:-1097,%22z%22:256,%22timestamp%22:41511,%22k%22:126,%22type%22:0%7D,%7B%22x%22:4454,%22y%22:224,%22z%22:1573,%22timestamp%22:41845,%22k%22:60,%22type%22:0%7D,%7B%22x%22:3416,%22y%22:-811,%22z%22:526,%22timestamp%22:41945,%22k%22:97,%22type%22:0%7D,%7B%22x%22:3270,%22y%22:-898,%22z%22:318,%22timestamp%22:42045,%22k%22:85,%22type%22:0%7D,%7B%22x%22:3783,%22y%22:5,%22z%22:535,%22timestamp%22:42155,%22k%22:70,%22type%22:0%7D,%7B%22x%22:3090,%22y%22:2282,%22z%22:684,%22timestamp%22:48217,%22k%22:113,%22type%22:0%7D,%7B%22x%22:3294,%22y%22:1173,%22z%22:986,%22timestamp%22:48316,%22k%22:106,%22type%22:0%7D,%7B%22x%22:4007,%22y%22:1124,%22z%22:1731,%22timestamp%22:48417,%22k%22:120,%22type%22:0%7D,%7B%22x%22:5142,%22y%22:2036,%22z%22:2822,%22timestamp%22:48520,%22k%22:61,%22type%22:0%7D,%7B%22x%22:3653,%22y%22:533,%22z%22:1329,%22timestamp%22:48622,%22k%22:112,%22type%22:0%7D,%7B%22x%22:2744,%22y%22:-391,%22z%22:419,%22timestamp%22:48726,%22k%22:79,%22type%22:0%7D,%7B%22x%22:3209,%22y%22:-12,%22z%22:820,%22timestamp%22:48827,%22k%22:73,%22type%22:0%7D,%7B%22x%22:2652,%22y%22:-959,%22z%22:76,%22timestamp%22:48929,%22k%22:123,%22type%22:0%7D,%7B%22x%22:5694,%22y%22:1554,%22z%22:2842,%22timestamp%22:49030,%22k%22:125,%22type%22:0%7D,%7B%22x%22:6489,%22y%22:2308,%22z%22:3622,%22timestamp%22:49141,%22k%22:98,%22type%22:0%7D,%7B%22x%22:6648,%22y%22:2733,%22z%22:3719,%22timestamp%22:49241,%22k%22:75,%22type%22:0%7D,%7B%22x%22:4118,%22y%22:861,%22z%22:1009,%22timestamp%22:49342,%22k%22:106,%22type%22:0%7D,%7B%22x%22:5264,%22y%22:1895,%22z%22:2123,%22timestamp%22:50014,%22k%22:87,%22type%22:0%7D,%7B%22x%22:6003,%22y%22:1852,%22z%22:2770,%22timestamp%22:50114,%22k%22:97,%22type%22:0%7D,%7B%22x%22:6620,%22y%22:2165,%22z%22:3379,%22timestamp%22:50216,%22k%22:96,%22type%22:0%7D,%7B%22x%22:5514,%22y%22:1053,%22z%22:2360,%22timestamp%22:50317,%22k%22:76,%22type%22:0%7D,%7B%22x%22:6459,%22y%22:2052,%22z%22:3419,%22timestamp%22:50418,%22k%22:93,%22type%22:0%7D,%7B%22x%22:7815,%22y%22:3415,%22z%22:4777,%22timestamp%22:50562,%22k%22:80,%22type%22:0%7D,%7B%22x%22:3217,%22y%22:-1083,%22z%22:247,%22timestamp%22:50662,%22k%22:99,%22type%22:0%7D,%7B%22x%22:3959,%22y%22:-257,%22z%22:1059,%22timestamp%22:50763,%22k%22:100,%22type%22:0%7D,%7B%22x%22:3995,%22y%22:-220,%22z%22:1092,%22timestamp%22:50873,%22k%22:124,%22type%22:0%7D,%7B%22x%22:4789,%22y%22:583,%22z%22:1767,%22timestamp%22:50973,%22k%22:88,%22type%22:0%7D,%7B%22x%22:4146,%22y%22:-67,%22z%22:1122,%22timestamp%22:51078,%22k%22:101,%22type%22:0%7D,%7B%22x%22:6652,%22y%22:2446,%22z%22:3630,%22timestamp%22:51628,%22k%22:123,%22type%22:0%7D,%7B%22x%22:4696,%22y%22:490,%22z%22:1674,%22timestamp%22:51733,%22k%22:66,%22type%22:0%7D]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEdvb2dsZSwgVnVsa2FuIDEuMy4wIChTd2lmdFNoYWRlciBEZXZpY2UgKFN1Ynplcm8pICgweDAwMDBDMERFKSksIFN3aWZ0U2hhZGVyIGRyaXZlcilHb29nbGUgSW5jLiAoR29vZ2xlKQ&dm_img_inter=%7B%22ds%22:[%7B%22t%22:10,%22c%22:%22YmUtcGFnZXItaXRlbQ%22,%22p%22:[2646,94,2192],%22s%22:[498,693,996]%7D],%22wh%22:[108,36,36],%22of%22:[1350.9999694824219,1964.6666259765625,245]%7D&w_rid=08452afe8ae52f550628eeb9b71088e1&wts=1706522666'
    # url = 'https://api.bilibili.com/x/space/wbi/arc/search?mid=400365390&ps=30&tid=0&pn=1&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEdvb2dsZSwgVnVsa2FuIDEuMy4wIChTd2lmdFNoYWRlciBEZXZpY2UgKFN1Ynplcm8pICgweDAwMDBDMERFKSksIFN3aWZ0U2hhZGVyIGRyaXZlcilHb29nbGUgSW5jLiAoR29vZ2xlKQ&dm_img_inter=%7B%22ds%22:[%7B%22t%22:2,%22c%22:%22Y2xlYXJmaXggZy1zZWFyY2ggc2VhcmNoLWNvbnRhaW5lcg%22,%22p%22:[1299,11,708],%22s%22:[351,813,1118]%7D,%7B%22t%22:2,%22c%22:%22d3JhcHBlcg%22,%22p%22:[759,37,1333],%22s%22:[33,4012,3118]%7D],%22wh%22:[24,8,8],%22of%22:[0,0,0]%7D&w_rid=e52fa26f2f6dba2a1b6a0a48fec5d2e9&wts=1706538329'
    # url = 'https://api.bilibili.com/x/space/wbi/arc/search?mid=400365390&ps=30&tid=0&pn=2&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEdvb2dsZSwgVnVsa2FuIDEuMy4wIChTd2lmdFNoYWRlciBEZXZpY2UgKFN1Ynplcm8pICgweDAwMDBDMERFKSksIFN3aWZ0U2hhZGVyIGRyaXZlcilHb29nbGUgSW5jLiAoR29vZ2xlKQ&dm_img_inter=%7B%22ds%22:[%7B%22t%22:2,%22c%22:%22Y2xlYXJmaXggZy1zZWFyY2ggc2VhcmNoLWNvbnRhaW5lcg%22,%22p%22:[1542,92,789],%22s%22:[144,606,704]%7D,%7B%22t%22:2,%22c%22:%22d3JhcHBlcg%22,%22p%22:[903,85,1381],%22s%22:[141,4120,3334]%7D],%22wh%22:[198,66,66],%22of%22:[475,950,475]%7D&w_rid=be4369e929b1284d54a68c0f761d6669&wts=1706539901'

    # url = 'https://api.bilibili.com/x/space/wbi/arc/search?mid=302299393&ps=30&tid=0&pn=1&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEdvb2dsZSwgVnVsa2FuIDEuMy4wIChTd2lmdFNoYWRlciBEZXZpY2UgKFN1Ynplcm8pICgweDAwMDBDMERFKSksIFN3aWZ0U2hhZGVyIGRyaXZlcilHb29nbGUgSW5jLiAoR29vZ2xlKQ&dm_img_inter=%7B%22ds%22:[%7B%22t%22:2,%22c%22:%22Y2xlYXJmaXggZy1zZWFyY2ggc2VhcmNoLWNvbnRhaW5lcg%22,%22p%22:[1401,45,742],%22s%22:[159,621,734]%7D,%7B%22t%22:2,%22c%22:%22d3JhcHBlcg%22,%22p%22:[957,103,1399],%22s%22:[140,4119,3332]%7D],%22wh%22:[162,54,54],%22of%22:[152,304,152]%7D&w_rid=fb53775dc5b7c41873a9006df3530863&wts=1706534726'
    # url = 'https://api.bilibili.com/x/space/wbi/arc/search?mid=302299393&ps=30&tid=0&pn=2&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEdvb2dsZSwgVnVsa2FuIDEuMy4wIChTd2lmdFNoYWRlciBEZXZpY2UgKFN1Ynplcm8pICgweDAwMDBDMERFKSksIFN3aWZ0U2hhZGVyIGRyaXZlcilHb29nbGUgSW5jLiAoR29vZ2xlKQ&dm_img_inter=%7B%22ds%22:[%7B%22t%22:2,%22c%22:%22Y2xlYXJmaXggZy1zZWFyY2ggc2VhcmNoLWNvbnRhaW5lcg%22,%22p%22:[1539,91,788],%22s%22:[322,784,1060]%7D,%7B%22t%22:2,%22c%22:%22d3JhcHBlcg%22,%22p%22:[690,14,1310],%22s%22:[449,4428,3950]%7D],%22wh%22:[129,43,43],%22of%22:[150,300,150]%7D&w_rid=fb2aaef625490ad08e8f10f563c89d79&wts=1706578758'
    # url = 'https://api.bilibili.com/x/space/wbi/arc/search?mid=302299393&ps=30&tid=0&pn=3&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[%7B%22x%22:1456,%22y%22:-52,%22z%22:0,%22timestamp%22:709,%22k%22:95,%22type%22:0%7D]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEludGVsLCBJbnRlbChSKSBJcmlzKFIpIFhlIEdyYXBoaWNzICgweDAwMDA0NkE2KSBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExKUdvb2dsZSBJbmMuIChJbnRlbC&dm_img_inter=%7B%22ds%22:[%7B%22t%22:0,%22c%22:%22%22,%22p%22:[288,96,96],%22s%22:[276,4504,4436]%7D],%22wh%22:[258,86,86],%22of%22:[115,230,115]%7D&w_rid=c1070e6751d2b13a1c5d95a82a61bb16&wts=1706583165'
    url = 'https://api.bilibili.com/x/space/wbi/arc/search?mid=302299393&ps=30&tid=0&pn=4&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&dm_img_list=[%7B%22x%22:56,%22y%22:-140,%22z%22:0,%22timestamp%22:1022,%22k%22:70,%22type%22:0%7D,%7B%22x%22:1033,%22y%22:-624,%22z%22:93,%22timestamp%22:1403,%22k%22:77,%22type%22:0%7D]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEludGVsLCBJbnRlbChSKSBJcmlzKFIpIFhlIEdyYXBoaWNzICgweDAwMDA0NkE2KSBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExKUdvb2dsZSBJbmMuIChJbnRlbC&dm_img_inter=%7B%22ds%22:[%7B%22t%22:0,%22c%22:%22%22,%22p%22:[99,33,33],%22s%22:[44,4272,3972]%7D],%22wh%22:[312,104,104],%22of%22:[481,962,481]%7D&w_rid=861d2ccf3b90bb8c20f21b185783bc49&wts=1706593978'

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    #     'Referer': 'https://space.bilibili.com/662609045/video?tid=0&pn=2&keyword=&order=pubdate',
    #     'Cookie': "buvid3=4F077F14-7A50-826A-07B1-E13EA6AB4AF448919infoc; b_nut=1694935048; i-wanna-go-back=-1; b_ut=7; _uuid=3A4B9E6A-DFBE-227A-10B47-AC656EF10AD2550259infoc; buvid4=0BA435A9-694D-D159-6E04-3CC62C4D9FC749832-023091715-vEypQIU/lka2gSe0HRe/Lw%3D%3D; DedeUserID=259090980; DedeUserID__ckMd5=17f29169a9316ab9; rpdid=|(kJYJlklJJm0J'uYmRmJl|mk; header_theme_version=CLOSE; hit-dyn-v2=1; enable_web_push=DISABLE; fingerprint=01a4536074ecc0c3148b21a4dd20e781; buvid_fp_plain=undefined; buvid_fp=01a4536074ecc0c3148b21a4dd20e781; CURRENT_FNVAL=16; CURRENT_QUALITY=64; home_feed_column=5; browser_resolution=1400-747; SESSDATA=a59c52a9%2C1722064662%2Ca20d8%2A12CjCDSQfG0qvETz8_XBoZdCdnJwpmSU4TA3owoJURQm2GkhHpuvJHzsOK1nJop0KECgASVnlWZDU3ajQ4bGFjbjNid1EtSk5MYTdPSXE3TS1DRkRzX1lSMHZUYXh5UEZONkluR2dNclRhaXFLTk5BOWxYLWxjbllfWi12Skw0NEt4RHhHRGxVbVd3IIEC; bili_jct=411555cec512d063e9813df69d52cceb; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDY3NzE4ODAsImlhdCI6MTcwNjUxMjYyMCwicGx0IjotMX0.5pXjXz0mH2IyHrzpCqWLLg2zcK_FsfZS_lxif7qLcdk; bili_ticket_expires=1706771820; PVID=1; b_lsid=10163C361_18D54A95F6B; sid=omd1mh0z; bp_video_offset_259090980=891996250162855944"
    # }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://space.bilibili.com/302299393/video',
        'Cookie': "buvid3=4F077F14-7A50-826A-07B1-E13EA6AB4AF448919infoc; b_nut=1694935048; i-wanna-go-back=-1; b_ut=7; _uuid=3A4B9E6A-DFBE-227A-10B47-AC656EF10AD2550259infoc; buvid4=0BA435A9-694D-D159-6E04-3CC62C4D9FC749832-023091715-vEypQIU/lka2gSe0HRe/Lw%3D%3D; DedeUserID=259090980; DedeUserID__ckMd5=17f29169a9316ab9; rpdid=|(kJYJlklJJm0J'uYmRmJl|mk; header_theme_version=CLOSE; hit-dyn-v2=1; enable_web_push=DISABLE; fingerprint=01a4536074ecc0c3148b21a4dd20e781; buvid_fp_plain=undefined; buvid_fp=01a4536074ecc0c3148b21a4dd20e781; CURRENT_FNVAL=16; CURRENT_QUALITY=64; home_feed_column=5; browser_resolution=1400-747; SESSDATA=a59c52a9%2C1722064662%2Ca20d8%2A12CjCDSQfG0qvETz8_XBoZdCdnJwpmSU4TA3owoJURQm2GkhHpuvJHzsOK1nJop0KECgASVnlWZDU3ajQ4bGFjbjNid1EtSk5MYTdPSXE3TS1DRkRzX1lSMHZUYXh5UEZONkluR2dNclRhaXFLTk5BOWxYLWxjbllfWi12Skw0NEt4RHhHRGxVbVd3IIEC; bili_jct=411555cec512d063e9813df69d52cceb; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDY3NzE4ODAsImlhdCI6MTcwNjUxMjYyMCwicGx0IjotMX0.5pXjXz0mH2IyHrzpCqWLLg2zcK_FsfZS_lxif7qLcdk; bili_ticket_expires=1706771820; bp_video_offset_259090980=891996250162855944; b_lsid=ED6410851_18D57EDC96A; sid=h0frutm4; PVID=1"
    }
    params = {

    }

    resp = requests.get(url=url, headers=headers)
    resp_json = resp.json()
    # pprint(resp_json)  # 验证成功
    vlist = resp_json['data']['list']['vlist']
    # pprint(vlist)  # 验证成功

    f = open('data.csv', mode='w', encoding='utf-8', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=['标题', 'bv', '时长', '播放量', '弹幕数量', '评论数量', '日期时间', ])
    csv_writer.writeheader()

    num = 1
    for item in vlist:
        print(f'\n\n\n=====================================req: url [{num}]=====================================')
        num += 1
        date_time = str(datetime.fromtimestamp(item['created']))
        bv = item['bvid']
        dit = {
            '标题': item['title'].replace(' ', '_'),
            'bv': bv,
            '时长': item['length'],
            '播放量': item['play'],
            '弹幕数量': item['video_review'],
            '评论数量': item['comment'],
            '日期时间': date_time
        }
        print(dit)
        csv_writer.writerow(dit)
        try:
            req_bilibili(bv)
        except Exception as e:
            print("请求过程中出现了一个异常:", e)

    # url_list = []
    # for v in vlist:
    #     bvid = v['bvid']
    #     url_list.append(bvid)
    # # print(url_list)  # 验证成功
    # url_list2 = ['https://www.bilibili.com/video/' + item for item in url_list]
    # print(url_list2)


if __name__ == '__main__':
    print('start...')
    # req_bilibili('BV15M4y1b7qc')
    req_bilibili_page()
    print('end...')
