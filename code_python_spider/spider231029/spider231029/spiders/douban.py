import scrapy
from scrapy import Selector, Request

from spider231029.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]

    # start_urls = ["https://movie.douban.com/top250"]
    def start_requests(self):
        for page in range(10):
            yield Request(
                url=f'https://movie.douban.com/top250?start={page * 25}&filter=',
                # callback=self.parse  # 默认的解析resp
            )

    def parse(self, response):
        sel = Selector(response)

        # 解析resp
        list_items = sel.css('#content > div > div.article > ol > li')
        for item in list_items:
            movie_item = MovieItem()

            # 详情页超链接进入
            detail_url = item.css('div.info > div.hd > a::attr(href)').extract_first()  # 拿到详情页的url 发起新req
            print(detail_url)

            movie_item['title'] = item.css('span.title::text').extract_first()
            movie_item['rank'] = item.css('span.rating_num::text').extract_first()
            movie_item['subject'] = item.css('span.inq::text').extract_first()

            yield Request(url=detail_url, callback=self.parse_detail, cb_kwargs={'item': movie_item})  # 解析详情页resp

        # 页面地下的横条 提取新url
        # list_hrefs = sel.css('#content > div > div.article > div.paginator > a::attr(href)')
        # for href in list_hrefs:
        #     url = href.extract()
        #     url = response.urljoin(url)
        #     yield Request(url)

        # pass

    def parse_detail(self, response, **kwargs):
        movie_item = kwargs['item']
        sel = Selector(response)
        movie_item['duration'] = sel.css('span[property="v:runtime"]::attr(content)').extract_first()
        movie_item['intro'] = sel.css('span[property="v:summary"]::text').extract_first()
        yield movie_item
