# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/13 14:37
# @File    ：demo2.py
# @Function:

import csv
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def sel_detail(num, hotel_name):
    """爬取详情页信息"""
    wd = webdriver.Chrome()
    wait = WebDriverWait(wd, 10)  # 设置最大等待时间（例如 10 秒）

    room_type = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='roomBody']/ul")))
    # print(room_type.text)  # 验证成功
    direct_child_li_elements = room_type.find_elements(By.XPATH, "./li")
    for li in direct_child_li_elements:
        # print(li.text)  # 验证成功
        print('\n========================================\n[datail]')
        room_name_parts = li.find_elements(By.XPATH,
                                           ".//div[contains(@class, 'roomName') or contains(@class, 'bedType')]")
        room_name_elements = ''.join([part.text for part in room_name_parts if
                                      part.text.strip() != '']).replace('查看详情', '')
        room_name_texts = [element for element in room_name_elements if element.strip()]
        room_name = ''.join(room_name_texts)  # 直接拼接，不加空格或其他字符
        print(f"Room Name: {room_name}")

        table = li.find_element(By.XPATH, ".//table/tr/td[@class='listRoomPolicies']/table")
        # print(table.text)  # 验证成功
        tr_list = table.find_elements(By.XPATH, "//tr[@class='introduce']")
        # for tr in tr_list:
        print('--------------------------------------------')
        product_name_elements = li.find_elements(By.XPATH, ".//ul[@class='tab']/li")
        product_names = '、'.join([name.text for name in product_name_elements if name.text.strip()])  # 提取产品名称
        breakfast_info = li.find_element(By.XPATH,
                                         ".//td[@class='c3']/div[contains(@class, 'outBox')]/span").text  # 提取早餐信息
        policy_info = li.find_element(By.XPATH,
                                      ".//td[@class='c4']/div/div[contains(@class, 'outBox')]/span").text  # 提取产品政策
        price_element = li.find_element(By.XPATH, ".//p[contains(@class, 'price')]/span")
        room_price = price_element.text  # 提取价格

        print(f"Price: {room_price}")
        print(f"Product Names: {product_names}")
        print(f"Breakfast: {breakfast_info}")
        print(f"Policy: {policy_info}")

        hotels_detail_info.append(
            [num, hotel_name, room_name, product_names, breakfast_info, policy_info, room_price])
        return hotels_detail_info

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
    """


def create_csv_detail_if_not_exists(csv_file):
    """ 表1：检查 CSV 文件是否存在，如果不存在则创建并添加表头 """
    if not os.path.isfile(csv_file):  # 如果文件不存在
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Num', 'Hotel Name', 'Room name', 'Product Name', 'Breakfast', 'Policy', 'Price'])
        print(f'Created {csv_file} and header written.')


def append_to_csv_detail(data_list, csv_file):
    """ 表1：将信息追加到已存在的 CSV 文件 """
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)
    print(f'Data appended to {csv_file}')


if __name__ == '__main__':
    print('start...')
    print('end...')
