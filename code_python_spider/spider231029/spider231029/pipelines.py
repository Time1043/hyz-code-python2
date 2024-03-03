# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re

import openpyxl
import pymysql


# useful for handling different item types with a single interface


class DescriptionCleaningPipeline:
    def process_item(self, item, spider):
        item['intro'] = self.clean_description(item['intro'])
        return item

    def clean_description(self, description):
        cleaned = re.sub(r'[\s\u3000]+', ' ', description).strip()
        return cleaned


class DbPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.23.128', port=3306,
            user='root', password='123',
            database='forSpider', charset='utf8mb4')
        self.cursor = self.conn.cursor()  # 游标
        self.data = []  # 批处理 准备的容器

    def open_spider(self, spider):  # 【1次】
        pass

    def close_spider(self, spider):  # 【1次】
        if len(self.data) > 0:
            self._write_to_db()
        self.conn.close()

    def process_item(self, item, spider):  # 【250次】
        title = item.get('title', ' ')
        rank = item.get('rank', 0)
        subject = item.get('subject', ' ')
        duration = item.get('duration', ' ')
        intro = item.get('intro', ' ')
        self.data.append((title, rank, subject, duration, intro))
        if len(self.data) == 100:  # 批处理 100条提交一次
            self._write_to_db()
            self.data.clear()
        return item

    def _write_to_db(self):
        self.cursor.executemany(
            'insert into tb_movie_top250 (title,rating,subject,duration,intro) values (%s,%s,%s,%s,%s)',
            self.data
        )
        self.conn.commit()


class ExcelPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()  # 工作薄
        self.ws = self.wb.active  # 工作表
        self.ws.title = 'top250'
        self.ws.append(('标题', '评分', '主题', '时长', '简介'))

    def open_spider(self, spider):  # 爬虫开始时【1次】
        pass

    def close_spider(self, spider):  # 关闭爬虫时保存文件【1次】
        self.wb.save('电影数据.xlsx')

    def process_item(self, item, spider):  # 处理数据  钩子方法【250次】
        title = item.get('title', ' ')
        rank = item.get('rank', 0)
        subject = item.get('subject', ' ')
        duration = item.get('duration', ' ')
        intro = item.get('intro', ' ')
        self.ws.append((title, rank, subject, duration, intro))
        return item
