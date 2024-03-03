# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/3/3 14:01
# @File    ：demo1_cookie.py
# @Function: 登录、拿cookie - session

import requests


def req_17k0():
    url = 'https://user.17k.com/ck/user/myInfo/103198945?bindInfo=1&appKey=2406394919'
    headers = {
        "Cookie": "GUID=5a13ad4b-30ec-4a33-aca5-d046fb4dd575; c_referer_17k=https://www.google.com.hk/; sajssdk_2015_cross_new_user=1; acw_sc__v2=65e41127c2d1db3ad99947df88cce34fa79471d5; Hm_lvt_9793f42b498361373512340937deb2a0=1709445437; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F05%252F45%252F89%252F103198945.jpg-88x88%253Fv%253D1709446152000%26id%3D103198945%26nickname%3Dtime1043%26e%3D1724998490%26s%3D5dc8d29e4deab031; tfstk=ewe6EjqDIFY_aLRMRNsUV_o9RgkbCP6PCniYqopwDAHTDxZYmquZgqPIp0UiMRkabysbJzqZgAebtKZumRSi3GDgjxDAzaWyhlqincCzIqBynojs1a7PU959vx_1z57ofwSfcw6Po1rhRQdWncYZnpsbBRwIfXCUq2e3EioI1vqtRaQ8dKhsyl3BHg-XU4MrrItIZKnIzMsBiIx-MpzYTrCavfnnXTSCAeOm6DmIzMsBiIctxcFPAMTBi; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22103198945%22%2C%22%24device_id%22%3A%2218e02e3051622bd-0f733ba99b0847-26001b51-3686400-18e02e3051722f1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%225a13ad4b-30ec-4a33-aca5-d046fb4dd575%22%7D; ssxmod_itna=Yq+xB7itKCux0Dl4iqob7XnC4fE9x7TYTWHRPDse1rDSxGKidDqxBWmlmhn0uiv5=bPe0QrDKS23tdOgdphoQb=Yehfom7x0aDbqGkP5GCbeDxOq0rD74irDDxD39D7PGmDinZuD7xU1S25CfxiOD7eDXxGCDQFh0xGWDiPD7xye4Z0CNDDzNDSNOQxDEDHzz67h=4D1Pp5xeD5D9x0CDla5yUoD0hLUNlHzXKdEEAF+o40OD0KmyxFwDBRCxUyOmFFaIcwxIjbr5j2qPP+Oe7tSlmi4herr6vn5TBUP5o2qDDa5zXpDD===; ssxmod_itna2=Yq+xB7itKCux0Dl4iqob7XnC4fE9x7TYTWH4ikAhqQQDunx0HbBq03BjU2RD6QBc6eyYiBydKP5WlcXt3=nlv6k13th32oTZOGot4tZrBhbsCompQx+/Y3/HOImOKyMaR4oQi9degCuDPYTaCOGQKCa8tpDTQ3T5HOvTXj5FRiiYxK57TriGsmg=/jOvm4HshYOGqnGx8YvEIzeOHEoI99WH6an6w2yig3cXYoBvxS2Am=W+m8nvBA5IxTKmikZvCp1CUxy8FFmWcn0quindWbu=XmFFbZyvktxCth2=zloT6TZ/I8Xi+HCWRG0mEmbC9T7jva0mnDa5SukYcDGuQRINeB7zhy/yNK0IlxqGeim+Ya+8/7Yq2zKD3D07NiKD7=DY9qeD; Hm_lpvt_9793f42b498361373512340937deb2a0=1709447604",
    }

    resp = requests.get(url=url, headers=headers)
    print(resp.text)  # 验证成功


def req_17k():
    session = requests.session()  # 会话 一系列的请求响应

    # 1 登录 拿cookie
    url_for_cookie = 'https://user.17k.com/ck/user/login'
    data = {
        'loginName': '17720900082',
        'password': 'H1665434994',
    }
    resp_for_cookie = session.post(url=url_for_cookie, data=data)
    # print(resp.text)  # 验证成功
    # print(resp_for_cookie.cookies)  # <RequestsCookieJar[...

    # 2 拿书架数据
    url = 'https://user.17k.com/ck/user/myInfo/103198945?bindInfo=1&appKey=2406394919'
    resp = session.get(url=url)  # 会话中有cookie
    # print(resp.text)  # 验证成功
    my_books = resp.json()['data']['recentFavorites']['lists']
    for book in my_books:
        book_id = book['bookId']
        book_name = book['bookName']
        print(book_id, book_name)


if __name__ == '__main__':
    print('start...')

    req_17k0()

    print('end...')
