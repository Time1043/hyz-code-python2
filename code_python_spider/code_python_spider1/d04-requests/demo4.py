# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/19 15:07
# @File    ：demo4.py
# @Function: cookies 用户身份

import requests

url = '''
https://mapi.guazi.com/car-source/carList/pcList?
versionId=0.0.0.0&sourceFrom=wap&deviceId=95237ad6-70b3-421d-b400-a9a6adeec728&
osv=Windows+10&minor=&sourceType=&ec_buy_car_list_ab=&location_city=&district_id=&
tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement=&
emission=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=&priceRange=0,
-1&tag_types=10012&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&
transfer_num=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&
page=2&pageSize=20&city_filter=12&city=12&guazi_city=12&qpres=728087225241174016&platfromSource=wap
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

cookies = '''
sessionid=b8e6ad6a-5bb6-4f45-fcfa-92168900b576; uuid=95237ad6-70b3-421d-b400-a9a6adeec728; 
gcinfo=%7B%22g_c%22%3A%2212%22%2C%22g_c_d%22%3A%22bj%22%2C%22g_c_n%22%3A%22%E5%8C%97%
E4%BA%AC%22%2C%22d_g_c%22%3A%221%22%2C%22l_c%22%3A-1%2C%22l_c_d%22%3A%22www%22%2C%22l_c_n%
22%3A%22%22%2C%22s_c%22%3A%2212%22%2C%22s_c_d%22%3A%22bj%22%2C%22s_c_n%22%3A%22%E5%8C%97%
E4%BA%AC%22%2C%22d_s_c%22%3A%221%22%7D; user_city_id=12; guazitrackersessioncadata=%
7B%22ca_kw%22%3A%22-%22%7D; 
puuid=94e38eeb-2beb-402b-ed61-35a1d5164031; cainfo=%7B%22ca_s%22%3A%
22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%
22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%
22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%2295237ad6-70b3-421d-b400-a9a6adeec728%22%7D
'''

resp = requests.get(url=url, headers=headers, cookies=cookies)
print(resp.text)
