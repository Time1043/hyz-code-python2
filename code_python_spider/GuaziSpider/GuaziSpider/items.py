# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # 汽车的名称、年份、里程、价格、首付、链接  内部实现是字典
    name = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    price = scrapy.Field()
    down_pay = scrapy.Field()
    link = scrapy.Field()
