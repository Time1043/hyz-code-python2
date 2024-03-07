import scrapy
from scrapy import Request

from ch02_ssr.items import MovieItem


class SsrSpider(scrapy.Spider):
    name = "ssr"
    allowed_domains = ["scrape.center"]
    # start_urls = [f"https://ssr1.scrape.center/page/{i}" for i in range(1, 11)]
    start_urls = ["https://ssr1.scrape.center"]

    def parse(self, response):
        for item in response.xpath("//div[@class='el-card item m-t is-hover-shadow']"):
            movie_item = MovieItem()
            movie_item["title"] = item.xpath(".//h2[@class='m-b-sm']/text()").get()
            movie_item["rank"] = item.xpath("//p[@class='score m-t-md m-b-n-sm']/text()").get().strip()
            movie_item["label"] = item.xpath(".//div[@class='categories']/button/span/text()").getall()
            movie_item["area"] = item.xpath("//div[@class='m-v-sm info']/span[1]/text()").get()
            movie_item["time"] = item.xpath("//div[@class='m-v-sm info']/span[3]/text()").get()
            movie_item["duration"] = item.xpath(".//div[@class='m-v-sm info'][2]/span/text()").get()

            yield movie_item

            # 提取新一页url 下一页按钮
            next_url = item.xpath("//a[@class='next']/@href").get()
            if next_url is not None:
                next_url = "https://ssr1.scrape.center" + next_url
                yield Request(next_url, callback=self.parse)  # 回调
