# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/11 12:10
# @File    ：demo1.py
# @Function:

import csv
import os
import re
import time
import urllib.parse
from datetime import datetime, timedelta

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 数据持久化、元数据
data_file = './data2/hotels_info.csv'  # 数据
memory_file = './data2/crawled_cities.txt'  # 记忆
num_after_next_city = 100  # 多少条数据后就下一个城市 并保存数据
hotels_info = []  # 表1 临时放在内存的数据 保存数据后置空
# 日期
current_date = datetime.now().date()  # 获取当前日期
in_date_str = current_date.strftime("%Y-%m-%d")  # 将当前日期转换为字符串
out_date_str = (current_date + timedelta(days=3)).strftime("%Y-%m-%d")  # 获取当前日期+3天，并转换为字符串
# 查询参数
cityId = 321
inDate = in_date_str
outDate = out_date_str
filterList = "1008_2,8888_1"
pageSize = 20
timestamp = int(time.time() * 1000)


def req_hotel():
    """ 失败 """
    url = 'https://www.ly.com/tapi/v2/list?city=321&filterList=1008_2&inDate=2024-02-11&outDate=2024-02-12&pageIndex=0&pageSize=8&reqScene=pchomerec'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.ly.com/hotel/',
        'Cookie': 'NewProvinceId=4; NCid=59; NewProvinceName=%E7%A6%8F%E5%BB%BA; NCName=%E6%B3%89%E5%B7%9E; Hm_lvt_64941895c0a12a3bdeb5b07863a52466=1707624143; qdid=-9999; 17uCNRefId=RefId=0&SEFrom=&SEKeyWords=; TicketSEInfo=RefId=0&SEFrom=&SEKeyWords=; CNSEInfo=RefId=0&tcbdkeyid=&SEFrom=&SEKeyWords=&RefUrl=; __tctma=144323752.1707622132364049.1707622132052.1707622132052.1707624141477.2; __tctmu=144323752.0.0; __tctmz=144323752.1707624141477.2.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); longKey=1707622132364049; __tctrack=0; route=a97a2a88fba4cfb78d93bebc5084a01e; H5CookieId=9f9d9534-7659-48bc-8e82-fd09a3125546; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1707622134,1707624201; hotel_lang=zh-cn; businessLine=hotel; H5Channel=mnoreferseo%2CSEO; indate=2024-02-11; outdate=2024-02-12; firsttime=1707624214691; abtkey=20f85050-b026-4954-839c-9c8919903e57; _tcudid_v2=g3Y-1bNhvpDLrWULKOe3pLcbEPdPEsr8vDTFvOt-oo0; us=userid=3137255270&nickName=%e5%90%8c%e7%a8%8b%e4%bc%9a%e5%91%98_5187E0B3C33&level=1&isUpgrade=true; nus=userid=3137255270&nickName=%e5%90%8c%e7%a8%8b%e4%bc%9a%e5%91%98_5187E0B3C33&level=1; mus=secsign=70fyjq97A10avM128x9t11lW4pl4wQ4N5cbRdVCB-_50SoDPD5ZBsOIJgQR3oVf-7_lrWV9VYISFkblAa2GT92cw**; passport_login_state=pageurl=%3fcodeParm%3d074171104114094071122085151012197045234130202214; cnUser=userid=3137255270&token=121104136099220086189022088250169036216247081231067054037057145072163176188211135229113167187045143148159034217052144200190034111010134244178163175120098196003046056059023020164040255194025105003190100042154025196082&loginType=passport&secsign=70fyjq97A10avM128x9t11lW4pl4wQ4N5cbRdVCB-_50SoDPD5ZBsOIJgQR3oVf-7_lrWV9VYISFkblAa2GT92cw**&authcode=F9872AE1FF8EB3CC67209D1B1910F3C9; CNMember=MemberId%3Dundefined; Hm_lpvt_64941895c0a12a3bdeb5b07863a52466=1707624617; __tctmc=144323752.205791637; __tctmd=144323752.164400958; __tctmb=144323752.4220509143072897.1707624352026.1707624614698.7; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1707624737; lasttime=1707624737327; JSESSIONID=635FD03A3CE3C2FDEF7655F1710B3DF9',
    }
    resp = requests.get(url=url, headers=headers)
    resp_json = resp.json()
    print(resp_json)

    hotel_list = resp_json['data']['hotelList']
    for hotel in hotel_list:
        hotel_id = hotel['hotelId']
        hotel_name = hotel['hotelName']
        recall_reason = hotel['recallReason'][0]
        star_level_des = hotel['starLevelDes']
        comment_main_tag = hotel['commentMainTag']
        price = hotel['price']
        price_decimal = hotel['priceDecimal']
        print(hotel_id, hotel_name, recall_reason, star_level_des, comment_main_tag, price, price_decimal)


def sel_hotel(city):
    """ 用selenium爬取酒店价格数据 """
    url_template = f"https://www.ly.com/hotel/hotellist?cityId={cityId}&city={city}&inDate={inDate}&outDate={outDate}&filterList={filterList}&pageSize={pageSize}&t={timestamp}"

    wd = webdriver.Chrome()
    wait = WebDriverWait(wd, 10)  # 设置最大等待时间（例如 10 秒）
    wd.get(url_template)  # 打开网址
    # wd.get('https://www.ly.com/hotel/')

    # 携带cookie
    cookie_str = 'NewProvinceId=4; NCid=59; NewProvinceName=%E7%A6%8F%E5%BB%BA; NCName=%E6%B3%89%E5%B7%9E; Hm_lvt_64941895c0a12a3bdeb5b07863a52466=1707624143; qdid=-9999; 17uCNRefId=RefId=0&SEFrom=&SEKeyWords=; TicketSEInfo=RefId=0&SEFrom=&SEKeyWords=; CNSEInfo=RefId=0&tcbdkeyid=&SEFrom=&SEKeyWords=&RefUrl=; __tctma=144323752.1707622132364049.1707622132052.1707622132052.1707624141477.2; __tctmu=144323752.0.0; __tctmz=144323752.1707624141477.2.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); longKey=1707622132364049; __tctrack=0; route=a97a2a88fba4cfb78d93bebc5084a01e; H5CookieId=9f9d9534-7659-48bc-8e82-fd09a3125546; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1707622134,1707624201; hotel_lang=zh-cn; businessLine=hotel; H5Channel=mnoreferseo%2CSEO; indate=2024-02-11; outdate=2024-02-12; firsttime=1707624214691; abtkey=20f85050-b026-4954-839c-9c8919903e57; _tcudid_v2=g3Y-1bNhvpDLrWULKOe3pLcbEPdPEsr8vDTFvOt-oo0; us=userid=3137255270&nickName=%e5%90%8c%e7%a8%8b%e4%bc%9a%e5%91%98_5187E0B3C33&level=1&isUpgrade=true; nus=userid=3137255270&nickName=%e5%90%8c%e7%a8%8b%e4%bc%9a%e5%91%98_5187E0B3C33&level=1; mus=secsign=70fyjq97A10avM128x9t11lW4pl4wQ4N5cbRdVCB-_50SoDPD5ZBsOIJgQR3oVf-7_lrWV9VYISFkblAa2GT92cw**; passport_login_state=pageurl=%3fcodeParm%3d074171104114094071122085151012197045234130202214; cnUser=userid=3137255270&token=121104136099220086189022088250169036216247081231067054037057145072163176188211135229113167187045143148159034217052144200190034111010134244178163175120098196003046056059023020164040255194025105003190100042154025196082&loginType=passport&secsign=70fyjq97A10avM128x9t11lW4pl4wQ4N5cbRdVCB-_50SoDPD5ZBsOIJgQR3oVf-7_lrWV9VYISFkblAa2GT92cw**&authcode=F9872AE1FF8EB3CC67209D1B1910F3C9; CNMember=MemberId%3Dundefined; Hm_lpvt_64941895c0a12a3bdeb5b07863a52466=1707624617; __tctmc=144323752.205791637; __tctmd=144323752.164400958; __tctmb=144323752.4220509143072897.1707624352026.1707624614698.7; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1707624737; lasttime=1707624737327; JSESSIONID=635FD03A3CE3C2FDEF7655F1710B3DF9'
    cookies = [x.split('=', 1) for x in cookie_str.split('; ')]
    cookies = [{'name': name, 'value': urllib.parse.unquote(value)} for name, value in cookies]
    for cookie in cookies:
        wd.add_cookie(cookie)
    wd.refresh()

    """
    # 经济连锁 点击更多
    more_hotels_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, 'hotellist?cityId=321')][contains(text(), '更多经济连锁酒店')]"))
    )  # 等待直到元素可被点击
    more_hotels_button.click()
    """

    # 进入详情页列表
    num = 1
    while True:
        if num > num_after_next_city:
            append_to_csv(hotels_info, data_file)  # 将数据写入csv
            hotels_info.clear()  # 内存数据置空
            print('\n=======================================================\n[next city]')
            break

        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "listBox")))
            hotels = wd.find_elements(by=By.XPATH, value='//ul[@class="listBox"]/li')  # 定位所有酒店信息的 <li> 元素
            for hotel in hotels:
                hotel_name = get_element_text_safe(hotel, './/p[@class="hotelName"]/a/span[@class="name"]')
                hotel_price = get_element_text_safe(hotel, './/div[@class="priceMsg fr"]/p[@class="newPrice"]')
                hotel_rating = get_element_text_safe(hotel,
                                                     './/div[@class="userEval fr"]/div[@class="scoreComment"]/p[@class="score mb5"]/em')
                comments_count = get_element_text_safe(hotel,
                                                       './/div[@class="userEval fr"]/div[@class="scoreComment"]/p[@class="comment mb10"]')
                hotel_address = get_element_text_safe(hotel, './/p[@class="position"]/span[1]')
                href_value = hotel.find_element(By.XPATH, "//a[@data-v-0b8539fe]").get_attribute('href')  # 超链接详情页

                print(
                    f'[{num}]  酒店名称: {hotel_name}, 价格: {hotel_price}, 评分: {hotel_rating}, 评论数: {comments_count}, 地址: {hotel_address}, 超链接：{href_value}')
                hotels_info.append([num, hotel_name, hotel_price, hotel_rating, comments_count, hotel_address, href_value])
                num += 1
        except Exception as e:
            print("点击下一页时发生错误:", e)

        # 使用显式等待确保“下一页”按钮是可点击的
        try:
            next_page = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@class="page" and contains(text(), "下一页")]'))
            )
            next_page.click()
            wait.until(EC.staleness_of(next_page))  # 等待下一页完全加载
        except (NoSuchElementException, TimeoutException) as e:
            print("无法找到下一页按钮，或按钮不可点击:", e)
        except Exception as e:
            print("点击下一页时发生错误:", e)

    # input('等待回车结束程序')


def get_element_text_safe(webElement, xpath):
    """ 辅助函数：在html中拿数据 """
    try:
        return webElement.find_element(By.XPATH, xpath).text
    except NoSuchElementException:
        return ""  # 如果没有找到元素，返回空字符串


def create_csv_if_not_exists(csv_file):
    """ 表1：检查 CSV 文件是否存在，如果不存在则创建并添加表头 """
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)
    if not os.path.isfile(csv_file):  # 如果文件不存在
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Num', 'Hotel Name', 'Price', 'Rating', 'Comments Count', 'Address', 'Href'])
        print(f'Created {csv_file} and header written.')
    else:
        print(f'{csv_file} already exists.')

def append_to_csv(data_list, csv_file):
    """ 表1：将信息追加到已存在的 CSV 文件 """
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)
    print(f'Data appended to {csv_file}')


def req_city_id():
    """ 抓包，拿去城市id """
    url = 'https://file.40017.cn/tcweb/pc/public/js/common/common.0.7.5.js?v=2024013101'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    resp = requests.get(url=url, headers=headers)
    resp_html = resp.text
    # print(resp_html)

    pattern_city_id = r'<ul class="rcc-ban">(.*?),'
    match = re.search(pattern_city_id, resp_html)  # 使用正则表达式搜索文本
    if match:
        # print("找到的关键信息:", match.group(1))
        pattern_city_id = r'<span cityid="(\d+)"[^>]*>([^<]+)</span>'
        matches = re.findall(pattern_city_id, match.group(1))
        city_dict = {name: id for id, name in matches}
        # print(city_dict)  # 验证成功
        return city_dict
    else:
        print("没有找到关键信息")


def init_crawled_cities_file(file_name):
    """ 表0：检查文件是否存在，不存在则创建"""
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    try:
        open(file_name, 'x').close()  # 尝试创建文件，如果文件已存在则不做任何操作
        print(f"File '{file_name}' created.")
    except FileExistsError:
        print(f"File '{file_name}' already existed.")  # 文件已存在，不需要创建


def append_crawled_city(file_name, city):
    """ 表0：将新爬取的城市追加到文件中 """
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(city + '\n')


def get_crawled_cities(file_name):
    """ 表0：从文件中读取已爬取的城市列表 """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read().splitlines()  # 读取所有行并分割成列表
    except FileNotFoundError:
        return []  # 如果文件不存在，返回空列表


def sel_many_cities():
    create_csv_if_not_exists(data_file)  # 数据 表1
    init_crawled_cities_file(memory_file)  # 记忆

    crawled_cities = get_crawled_cities(memory_file)  # 已爬城市
    cities = req_city_id()  # 所有城市
    print(
        f'There are a total of {len(cities)} cities, and {len(crawled_cities)} cities have been completed. \n{crawled_cities} \n{cities}')

    for city, city_id in cities.items():
        if city in crawled_cities:
            print(f"Already crawled: {city}")
            continue

        print('\n=======================================================\n[Crawling]')
        print(f"Crawling city: {city} with ID: {city_id}")
        sel_hotel(city_id)  # 爬虫
        append_crawled_city(memory_file, city)  # 更新已爬取的城市列表


if __name__ == '__main__':
    print('start...')

    # req_hotel()
    # sel_hotel()  # 单个城市
    sel_many_cities()  # 多个城市

    print('end...')
