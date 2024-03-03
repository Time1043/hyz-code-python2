# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/10 23:56
# @File    ：demo.py
# @Function:

import requests
import parsel





def req_youji_list():
    url = 'https://m.ctrip.com/restapi/soa2/22670/getRecommendTravel?_fxpcqlniredt=09031087210320450945&x-traceID=09031087210320450945-1707580947648-9147262'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://you.ctrip.com/',
        'Cookie': 'GUID=09031087210320450945; nfes_isSupportWebP=1; UBT_VID=1707580434652.e4e8TqWMqs1k; MKT_CKID=1707580435223.89vq1.om3r; _RF1=180.233.69.156; _RSG=I4aR9SxDrM2kHmSan5bZJA; _RDG=284af58262fdab2b37349f74eb7d94ca49; _RGUID=25b537b7-096e-4112-a4e3-945c6473046e; MKT_Pagesource=PC; _bfaStatusPVSend=1; _ubtstatus=%7B%22vid%22%3A%221707580434652.e4e8TqWMqs1k%22%2C%22sid%22%3A1%2C%22pvid%22%3A11%2C%22pid%22%3A0%7D; _bfi=p1%3D0%26p2%3Dundefined%26v1%3D11%26v2%3D9; _bfaStatus=success; _jzqco=%7C%7C%7C%7C1707580435756%7C1.2037136763.1707580435231.1707580810683.1707580946878.1707580810683.1707580946878.undefined.0.0.10.10; _bfa=1.1707580434652.e4e8TqWMqs1k.1.1707580825080.1707580957809.1.12.0'
    }
    json_data = {"head": {"cid": "09031087210320450945", "ctok": "", "cver": "1.0", "lang": "01", "sid": "8888",
                          "syscode": "999", "auth": "", "xsid": "", "extension": []},
                 "districtId": 148, "sourceFrom": 0, "type": 3, "pageIndex": 1}
    resp = requests.post(url=url, headers=headers, json=json_data)
    resp_json = resp.json()
    # print(resp_json)  # 验证成功

    youji_url_list = resp_json['travelInfoList']
    # print(youji_url_list)  # 验证成功
    for youji_url in youji_url_list:
        title = youji_url['title']
        sub_content = youji_url['content']
        id = youji_url['id']
        picture_number = youji_url['pictureNumber']
        comment_number = youji_url['commentNumber']
        view_number = youji_url['viewNumber']
        author_name = youji_url['author']['name']
        url = youji_url['jumpUrl']
        print(title, sub_content, id, picture_number, comment_number, view_number, author_name, url)
        print('------------------------------------------------------------')
        req_youji_in(url)
        print('============================================================')


def req_youji_in(url):
    # url = 'https://you.ctrip.com/travels/101/4106672.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    resp = requests.get(url=url, headers=headers)
    detail_html = resp.text
    # print(detail_html)  # 信息在html中

    select = parsel.Selector(detail_html)
    like_number = select.css('#TitleLike > span').get()
    info = ', '.join(select.css('.ctd_content_controls.cf div span::text').getall())
    content = '\n'.join(select.css('.ctd_content > p::text').getall())
    print(f'[1]  {like_number}')
    print(f'[2]  {info}')
    print(f'[3]  {content}')


def req_hotel():
    url = 'https://m.ctrip.com/restapi/soa2/21881/json/HotelSearch?testab=5ebee1c51f0b200dbbbe4452a337bf19c59ea6494521267f84a5a319dcd5d49c'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://hotels.ctrip.com/',
        'Cookie': 'GUID=09031087210320450945; nfes_isSupportWebP=1; UBT_VID=1707580434652.e4e8TqWMqs1k; MKT_CKID=1707580435223.89vq1.om3r; _RSG=I4aR9SxDrM2kHmSan5bZJA; _RDG=284af58262fdab2b37349f74eb7d94ca49; _RGUID=25b537b7-096e-4112-a4e3-945c6473046e; MKT_Pagesource=PC; _bfaStatusPVSend=1; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; cticket=3FF2C88DD3DBF8B86782D8BB80E10207771C8B5F7BE592A3EB68E440604C873B; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; DUID=u=E55ADB805D428882815526A84CE9C16E&v=0; IsNonUser=F; UUID=8A3932004B394DFAA321FC7B91AB9625; IsPersonalizedLogin=F; _RF1=180.233.69.156; _ubtstatus=%7B%22vid%22%3A%221707580434652.e4e8TqWMqs1k%22%2C%22sid%22%3A3%2C%22pvid%22%3A28%2C%22pid%22%3A0%7D; _bfi=p1%3D0%26p2%3D290602%26v1%3D28%26v2%3D18; _bfaStatus=success; librauuid=; _bfa=1.1707580434652.e4e8TqWMqs1k.1.1707621335830.1707621337133.3.31.102002; _jzqco=%7C%7C%7C%7C1707580435756%7C1.2037136763.1707580435231.1707621302451.1707621337301.1707621302451.1707621337301.undefined.0.0.36.36'
    }
    json_data = """
    {"searchCondition":{"sortType":"","adult":1,"child":0,"age":"","pageNo":1,"optionType":"City","optionId":2,"lat":0,"destination":"上海","keyword":"","cityName":"上海","lng":0,"cityId":2,"checkIn":"2024-02-11","checkOut":"2024-02-12","roomNum":1,"mapType":"","travelPurpose":0,"countryId":1,"url":"http://hotels.ctrip.com/hotels/list?countryId=1&city=2&checkin=2024/02/11&checkout=2024/02/12&optionId=2&optionType=City&directSearch=0&display=%E4%B8%8A%E6%B5%B7&crn=1&adult=1&children=0&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=1&","pageSize":10,"timeOffset":28800,"radius":0,"directSearch":0,"signInHotelId":0,"signInType":0},"filterCondition":{"star":[],"rate":0,"breakfast":[],"bookable":[],"zone":[],"landmark":[],"metro":[],"airportTrainstation":[],"location":[],"brand":[],"feature":[],"category":[],"amenty":[],"discount":[],"cityId":[],"payType":[],"bookPolicy":[],"bedType":[],"priceRange":{"highPrice":-1,"lowPrice":0,"curr":"CNY"},"priceType":"","promotion":[],"rateCount":[],"hotArea":[],"ctripService":[],"applicablePeople":[],"hotPoi":[],"covid":[]},"ssr":false,"genk":true,"genKeyParam":{"a":0,"b":"2024-02-11","c":"2024-02-12","d":"zh-cn","e":2},"pageTraceId":"791cab9b-3443-4937-9f04-d24fec796d1b","head":{"Locale":"zh-CN","Currency":"CNY","Device":"PC","UserIP":"180.233.69.156","Group":"ctrip","ReferenceID":"","UserRegion":"CN","AID":null,"SID":null,"Ticket":"","UID":"","IsQuickBooking":"","ClientID":"09031087210320450945","OUID":null,"TimeZone":"8","P":"89682257465","PageID":"102002","Version":"","HotelExtension":{"WebpSupport":true,"group":"CTRIP","Qid":"257507847785","hasAidInUrl":false,"hotelUuidKey":"4dHrTQYlki76ioNKLteS9E7pIgyF7rppxNYf4JopI6BYQ7YqlEBme05Ypy9YGbiZGWdUwpLeNQEzcjDNWQcj1BiFQikYHmiUUK1nRLQYcTw8hwzpjMJXOjo9w04vP6jfJbtj9ljozvPkjSJ9ny8BWlZyFzjfFvDhe8bYFcjPpysLwgcv4MjhYpPvhUeoAvzSyAOj1ZvsLEPfvaOWpfjcdj5bygtEzYdBEpNjsbeQTY1TifPwSPRanEpTWTLYN1y5ByGYskv0lRg1RXXxp5WS0wMYM9wT5Wq7wg1JnJOQjTY6QjnoEzfYf5vFnYoBylsjpov5De9gY8GjoXyLJldvG1YktyzhjbTv37eHcYb7jLHygJFnYDavNFW0BWmUEs8vZnRSYLyFGEZGi9Mvn5ezXYLdi36YZSYpGj18YHYUHWkdWlcxkPY1crlAEBY6kvT4ykqr1Bxl0i63v7YHZr76xS7ISbYhBifFiAbilXjlNxHmyXzKhYFTEZSE9kEXkyLpygHYtAwfqwUkyzTYs1waLxDzEXNrnYZyX8wflWk5Rfpy56WZFyPowOkYlsRoli4QiDSw3zys3RNawcmIAypdJPYhXjdDwfawQPJsly3crkYZHy97eNGrqnRknycpWoZyf5JQoj1tWPQE9Oih6EpcwldJZUY0PJm1xFnwDY6Hwl7rZdIspjaGw9fvZmjDGifhr0pIFY5SiNgr3EmqRsDEUkE43WBben1v3twptW5gESlW3me7YAqRcTEH4YOzRf7EbqE91WzBeOZvX3RqpYDSx8oKZQiDYhaigHJ5AWtqR9mytsW49yOmwbkYH3Rh4iDHipMwtOyf5RGcJXBym9w8Xj0YXGKApWqhjFTEGmjFSWGdWzPWT3Ya5YQgYFSRGnYq1WpMY87Y45YODjzLesXEHNW7UeP1wUHeT4jfoYFAyAoEgAj8NEocr47jGowl7ydTv6SW8SESYA6R8FWpmW6BWzgWn6YqYgQvl1ESLItfvmtEUzWF1y3QjoJTQvoMEz7W97yALjgHrMfeX1YfY01rBjtBJncEQTEohE9ORXOEqXJtkIBgEgYZBi3ZInqyc8YO7EolEO8YbmYAdYokYsjqtYNa"},"Frontend":{"vid":"1707580434652.e4e8TqWMqs1k","sessionID":"3","pvid":"31"}},"ServerData":""}
    """
    resp = requests.post(url=url, headers=headers, data=json_data)
    resp_json = resp.json()
    print(resp_json)

    hotel_list = resp_json['Response']['hotelList']['list']
    for hotel in hotel_list:
        hotel_name = hotel['base']['hotelName']
        hotel_tags = hotel['base']['tags']
        price = hotel['money']['price']
        price_delete = hotel['money']['priceDelete']
        position = hotel['position']
        print(hotel_name, hotel_tags, price, price_delete, position)


if __name__ == '__main__':
    print('start...')

    # req_youji_list()
    # req_youji_in()

    req_hotel()

    print('end...')
