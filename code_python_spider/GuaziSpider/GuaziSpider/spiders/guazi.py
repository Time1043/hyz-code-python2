import requests
import scrapy

from GuaziSpider.items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = "guazi"
    allowed_domains = ["www.guazi.com"]

    start_urls = ["https://www.guazi.com/buy"]

    def parse(self, response):
        list_div = response.xpath('//div[@class="carlist-content clearfix"]/div')
        for div in list_div:
            item = GuaziItem()
            item['name'] = div.xpath('./h5/text()').get()
            item['year'] = div.xpath('./div[@class="card-tags"]/text()').get()
            item['mileage'] = div.xpath('./div[@class="card-tags"]/span[@class="gzfont"]/text()').get()
            item['price'] = div.xpath('./div[@class="card-price"]/p/span[@class="gzfont"]/text()').get()
            item['down_pay'] = div.xpath('./div[@class="card-price"]/em[@class="price-firstpay gzfont"]/text()').get()
            item['link'] = ' '
            yield item  # 把抓取的数据交给管道
