# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/11 19:58
# @File    ：demo1test.py
# @Function:

import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def sel_detail(url_detail):
    """爬取详情页信息"""
    wd = webdriver.Chrome()
    wait = WebDriverWait(wd, 10)  # 设置最大等待时间（例如 10 秒）
    wd.get(url_detail)

    # 携带cookie
    cookie_str = 'NewProvinceId=4; NCid=59; NewProvinceName=%E7%A6%8F%E5%BB%BA; NCName=%E6%B3%89%E5%B7%9E; Hm_lvt_64941895c0a12a3bdeb5b07863a52466=1707624143; qdid=-9999; 17uCNRefId=RefId=0&SEFrom=&SEKeyWords=; TicketSEInfo=RefId=0&SEFrom=&SEKeyWords=; CNSEInfo=RefId=0&tcbdkeyid=&SEFrom=&SEKeyWords=&RefUrl=; __tctma=144323752.1707622132364049.1707622132052.1707622132052.1707624141477.2; __tctmu=144323752.0.0; __tctmz=144323752.1707624141477.2.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); longKey=1707622132364049; __tctrack=0; route=a97a2a88fba4cfb78d93bebc5084a01e; H5CookieId=9f9d9534-7659-48bc-8e82-fd09a3125546; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1707622134,1707624201; hotel_lang=zh-cn; businessLine=hotel; H5Channel=mnoreferseo%2CSEO; indate=2024-02-11; outdate=2024-02-12; firsttime=1707624214691; abtkey=20f85050-b026-4954-839c-9c8919903e57; _tcudid_v2=g3Y-1bNhvpDLrWULKOe3pLcbEPdPEsr8vDTFvOt-oo0; us=userid=3137255270&nickName=%e5%90%8c%e7%a8%8b%e4%bc%9a%e5%91%98_5187E0B3C33&level=1&isUpgrade=true; nus=userid=3137255270&nickName=%e5%90%8c%e7%a8%8b%e4%bc%9a%e5%91%98_5187E0B3C33&level=1; mus=secsign=70fyjq97A10avM128x9t11lW4pl4wQ4N5cbRdVCB-_50SoDPD5ZBsOIJgQR3oVf-7_lrWV9VYISFkblAa2GT92cw**; passport_login_state=pageurl=%3fcodeParm%3d074171104114094071122085151012197045234130202214; cnUser=userid=3137255270&token=121104136099220086189022088250169036216247081231067054037057145072163176188211135229113167187045143148159034217052144200190034111010134244178163175120098196003046056059023020164040255194025105003190100042154025196082&loginType=passport&secsign=70fyjq97A10avM128x9t11lW4pl4wQ4N5cbRdVCB-_50SoDPD5ZBsOIJgQR3oVf-7_lrWV9VYISFkblAa2GT92cw**&authcode=F9872AE1FF8EB3CC67209D1B1910F3C9; CNMember=MemberId%3Dundefined; Hm_lpvt_64941895c0a12a3bdeb5b07863a52466=1707624617; __tctmc=144323752.205791637; __tctmd=144323752.164400958; __tctmb=144323752.4220509143072897.1707624352026.1707624614698.7; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1707624737; lasttime=1707624737327; JSESSIONID=635FD03A3CE3C2FDEF7655F1710B3DF9'
    cookies = [x.split('=', 1) for x in cookie_str.split('; ')]
    cookies = [{'name': name, 'value': urllib.parse.unquote(value)} for name, value in cookies]
    for cookie in cookies:
        wd.add_cookie(cookie)
    wd.refresh()

    room_type = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='roomBody']/ul")))
    # print(room_type.text)  # 验证成功
    direct_child_li_elements = room_type.find_elements(By.XPATH, "./li")
    for li in direct_child_li_elements:
        # print(li.text)  # 验证成功
        print('=================')
        room_name_parts = li.find_elements(By.XPATH,
                                           ".//div[contains(@class, 'roomName') or contains(@class, 'bedType')]")
        room_name_elements = ''.join([part.text for part in room_name_parts if part.text.strip() != '']).replace(
            '查看详情', '')
        room_name_texts = [element for element in room_name_elements if element.strip()]
        room_name = ''.join(room_name_texts)  # 直接拼接，不加空格或其他字符
        print(f"Room Name: {room_name}")

        table = li.find_element(By.XPATH, ".//table/tr/td[@class='listRoomPolicies']/table")
        # print(table.text)  # 验证成功

        """
        """
        try:
            tr_list = table.find_elements(By.XPATH, ".//tr[@class='introduce']")
            for tr in tr_list:
                print('--------------------------------------------')
                product_name_elements = tr.find_elements(By.XPATH, ".//ul[@class='tab']/li")
                product_names = '、'.join([name.text for name in product_name_elements if name.text.strip()])  # 提取产品名称
                breakfast_info = tr.find_element(By.XPATH,
                                                 ".//td[@class='c3']/div[contains(@class, 'outBox')]/span").text  # 提取早餐信息
                policy_info = tr.find_element(By.XPATH,
                                              ".//td[@class='c4']/div/div[contains(@class, 'outBox')]/span").text  # 提取产品政策
                room_price = tr.find_element(By.XPATH, ".//p[contains(@class, 'price')]/span").text  # 提取价格

                print(f"Product Names: {product_names}")
                print(f"Breakfast: {breakfast_info}")
                print(f"Policy: {policy_info}")
                print(f"Price: {room_price}")
        except Exception as e:
            print(f'error: {e}')

        """
        # 没有点击抓不到
        room_detail = table.find_elements(By.XPATH, "//tr[@class='listRoomDetail']")
        for detail in room_detail:
            time.sleep(10)
            print('--------------------------------------------')
            room_info_spans = detail.find_element(By.XPATH, "//div[@class='roomInfo']/span")
            print(room_info_spans.text)

            # area = detail.find_element(By.XPATH, "//span[contains(., '面积')]").text  # 提取面积
            # bed_type = detail.find_element(By.XPATH, "//span[contains(., '床型')]").text  # 提取床型
            # window = detail.find_element(By.XPATH, "//span[contains(., '窗户')]").text  # 提取窗户情况
            # floor = detail.find_element(By.XPATH, "//span[contains(., '楼层')]").text  # 提取楼层
            # smoking_policy = detail.find_element(By.XPATH, "//span[contains(., '吸烟')]").text  # 提取吸烟政策
            # amenities = detail.find_element(By.XPATH, "//span[contains(., '便利设施')]").text  # 提取便利设施
            # bathroom_facilities = detail.find_element(By.XPATH, ".//span[contains(., '卫浴')]").text  # 提取卫浴设施
            # multimedia = detail.find_element(By.XPATH, ".//span[contains(., '电器')]").text  # 提取电器多媒体
            # food_beverage = detail.find_element(By.XPATH, ".//span[contains(., '食品')]").text  # 提取食品饮品
            # view = detail.find_element(By.XPATH, ".//span[contains(., '景观')]").text  # 提取室外景观
            # children_extra_bed = detail.find_element(By.XPATH, ".//span[contains(., '儿童')]").text  # 提取儿童及加床政策
            # print(
            #     f"面积: {area}, 床型: {bed_type}, 窗户: {window}, 楼层: {floor}, 吸烟政策: {smoking_policy}, 便利设施: {amenities}, 卫浴设施: {bathroom_facilities}, 电器多媒体: {multimedia}, 食品饮品: {food_beverage}, 室外景观: {view}, 儿童及加床: {children_extra_bed}")
        """

    """
    """
    try:
        open_details = wd.find_elements(By.XPATH, "//p[@class='openDetail']")
        room_info_switches = wd.find_elements(By.XPATH, "//i[@class='roomInfoDetSwitch']")
        print(len(open_details))
        print(len(room_info_switches))
        for i in range(len(open_details)):
            ActionChains(wd).move_to_element(open_details[i]).click(open_details[i]).perform()
            time.sleep(10)
            ActionChains(wd).move_to_element(room_info_switches[i]).click(room_info_switches[i]).perform()
            time.sleep(10)
            room_detail_div = wd.find_elements(By.XPATH, "//div[contains(@class, 'roomDetail on')]")[i]
            print('--------------------------------------------')
            room_detail_text = room_detail_div.text
            processed_text = '  '.join(
                [f"{line.rstrip('.')}。" for line in room_detail_text.split('\n') if line.strip()])
            print(processed_text)

        # for detail in open_details:
        #     ActionChains(wd).move_to_element(detail).click(detail).perform()
        #     time.sleep(10)  # 等待页面反应，根据实际情况调整等待时间
        # for switch in room_info_switches:
        #     ActionChains(wd).move_to_element(switch).click(switch).perform()
        #     time.sleep(10)  # 等待页面反应，根据实际情况调整等待时间
    except Exception as e:
        print(f'error: {e}')
        # room_detail_div = wd.find_element(By.XPATH, "//div[contains(@class, 'roomDetail on')]")
        # print('--------------------------------------------')
        # print(room_detail_div.text)


if __name__ == '__main__':
    print('start...')

    # url_detail = 'https://www.ly.com/hotel/hoteldetail?hotelId=92365962&filterList=&inDate=2024-02-11&outDate=2024-02-14&traceToken=%7C%2a%7CcityId%3A1204%7C%2a%7CqId%3A4017c2f6-13d2-405e-9dbe-99bec563edd0%7C%2a%7Cst%3Acity%7C%2a%7CsId%3A1204%7C%2a%7Cscene_ids%3A0%7C%2a%7Csmz%3AA%7C%2a%7Cbkt%3Ar3%7C%2a%7Cpos%3A0%7C%2a%7ChId%3A92365962%7C%2a%7CTp%3Adefault%7C%2a%7Cpage_index%3A4%7C%2a%7Cpage_size%3A20%7C%2a%7C&prc=138'
    url_detail = 'https://www.ly.com/hotel/hoteldetail?hotelId=51201336&filterList=&inDate=2024-02-11&outDate=2024-02-12&traceToken=%7C%2a%7CcityId%3A1201%7C%2a%7CqId%3A1e17ba38-2edd-428a-ae21-0291d86245f9%7C%2a%7Cst%3Acity%7C%2a%7CsId%3A1201%7C%2a%7Cscene_ids%3A0%7C%2a%7Csmz%3AB%7C%2a%7Cbkt%3Ar1%7C%2a%7Cpos%3A0%7C%2a%7ChId%3A51201336%7C%2a%7CTp%3Adefault%7C%2a%7Cpage_index%3A0%7C%2a%7Cpage_size%3A20%7C%2a%7C&prc=600'
    sel_detail(url_detail)

    print('end...')
