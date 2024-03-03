# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/20 21:37
# @File    ：case7-12306.py
# @Function:


import requests

# 1 拿到url
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2023-10-24&leftTicketDTO.from_station=XMS&leftTicketDTO.to_station=SZQ&purpose_codes=0X00'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Cookie': '_uab_collina=169780921102478792169898; JSESSIONID=DE7731F7990D6B5EE301175A3473AA2B; BIGipServerotn=585629962.64545.0000; fo=bm80grwzexne1m11fL0ZaNbG99R-rxYz101cK3HJXax6LLQPvpYvdbP7Ox_lrHqB-VD99VyvgdUg_qqAYU1lVQ0OOpXq23gu6YrcHqLqBlAqwTvfx_oAcyFSjNDy5QCp2jqZ0V7RQ15zv4ohruxHeNph1sbPDT1Wi7xAncdhOJBfZ4FpCzP6vNrK3dU; BIGipServerpassport=770179338.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u53A6%u95E8%2CXMS; _jc_save_toStation=%u6DF1%u5733%2CSZQ; _jc_save_fromDate=2023-10-24; _jc_save_toDate=2023-10-20; _jc_save_wfdc_flag=dc',
}

# 2 模拟浏览器请求
resp = requests.get(url=url, headers=headers)

# print(resp.text)  # 存在乱码
# print(resp.content.decode('utf-8'))  # 网络可能存在问题，请您重试一下！
# print(resp.content.decode('utf-8'))  # 成功

# 3 解析数据
data_json = resp.json()
list_train = data_json['data']['result']
for train in list_train:
    print(train)
    print('-------------------------')