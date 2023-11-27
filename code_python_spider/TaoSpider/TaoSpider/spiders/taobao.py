import time
import scrapy
from scrapy.http import Response

from TaoSpider.items import TaospiderItem


class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["www.taobao.com"]

    # start_urls = ["https://www.taobao.com"]
    def start_requests(self):
        keywords = ['荧光笔', '2B铅笔', '三菱笔']
        # keywords = ['ipad', '小米手机', '红米手机', '苹果手机', '华为', 'oppo', 'vivo', '魅族']
        current_timestamp_milliseconds = int(time.time() * 1000)

        # for keyword in keywords:
        #     url = f'https://s.taobao.com/search?q={keyword}'
        #     yield scrapy.Request(url=url, meta={'proxy': '8.219.5.240:9992'})

        for keyword in keywords:
            for page in range(10):
                url = f'https://s.taobao.com/search?page={page}&q={keyword}'
                yield scrapy.Request(url=url, meta={'proxy': '8.219.5.240:9992'})

        # for keyword in keywords:
        #     for page in range(2):
        #         url = f'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.6.2&appKey=12574478&t={current_timestamp_milliseconds}&sign=800a31a0e4fbabd9478236d03ab36749&api=mtop.relationrecommend.WirelessRecommend.recommend&v=2.0&type=jsonp&dataType=jsonp&callback=mtopjsonp{page}&data=%7B%22appId%22%3A%2234385%22%2C%22params%22%3A%22%7B%5C%22device%5C%22%3A%5C%22HMA-AL00%5C%22%2C%5C%22isBeta%5C%22%3A%5C%22false%5C%22%2C%5C%22grayHair%5C%22%3A%5C%22false%5C%22%2C%5C%22from%5C%22%3A%5C%22nt_history%5C%22%2C%5C%22brand%5C%22%3A%5C%22HUAWEI%5C%22%2C%5C%22info%5C%22%3A%5C%22wifi%5C%22%2C%5C%22index%5C%22%3A%5C%224%5C%22%2C%5C%22rainbow%5C%22%3A%5C%22%5C%22%2C%5C%22schemaType%5C%22%3A%5C%22auction%5C%22%2C%5C%22elderHome%5C%22%3A%5C%22false%5C%22%2C%5C%22isEnterSrpSearch%5C%22%3A%5C%22true%5C%22%2C%5C%22newSearch%5C%22%3A%5C%22false%5C%22%2C%5C%22network%5C%22%3A%5C%22wifi%5C%22%2C%5C%22subtype%5C%22%3A%5C%22%5C%22%2C%5C%22hasPreposeFilter%5C%22%3A%5C%22false%5C%22%2C%5C%22prepositionVersion%5C%22%3A%5C%22v2%5C%22%2C%5C%22client_os%5C%22%3A%5C%22Android%5C%22%2C%5C%22gpsEnabled%5C%22%3A%5C%22false%5C%22%2C%5C%22searchDoorFrom%5C%22%3A%5C%22srp%5C%22%2C%5C%22debug_rerankNewOpenCard%5C%22%3A%5C%22false%5C%22%2C%5C%22homePageVersion%5C%22%3A%5C%22v7%5C%22%2C%5C%22searchElderHomeOpen%5C%22%3A%5C%22false%5C%22%2C%5C%22search_action%5C%22%3A%5C%22initiative%5C%22%2C%5C%22sugg%5C%22%3A%5C%22_4_1%5C%22%2C%5C%22sversion%5C%22%3A%5C%2213.6%5C%22%2C%5C%22style%5C%22%3A%5C%22list%5C%22%2C%5C%22ttid%5C%22%3A%5C%22600000%40taobao_pc_10.7.0%5C%22%2C%5C%22needTabs%5C%22%3A%5C%22true%5C%22%2C%5C%22areaCode%5C%22%3A%5C%22CN%5C%22%2C%5C%22vm%5C%22%3A%5C%22nw%5C%22%2C%5C%22countryNum%5C%22%3A%5C%22156%5C%22%2C%5C%22m%5C%22%3A%5C%22pc%5C%22%2C%5C%22page%5C%22%3A{page}%2C%5C%22n%5C%22%3A48%2C%5C%22q%5C%22%3A%5C%22{keyword}%5C%22%2C%5C%22tab%5C%22%3A%5C%22all%5C%22%2C%5C%22pageSize%5C%22%3A%5C%2248%5C%22%2C%5C%22totalPage%5C%22%3A%5C%22100%5C%22%2C%5C%22totalResults%5C%22%3A%5C%2288661%5C%22%2C%5C%22sourceS%5C%22%3A%5C%220%5C%22%2C%5C%22sort%5C%22%3A%5C%22_coefp%5C%22%2C%5C%22bcoffset%5C%22%3A%5C%220%5C%22%2C%5C%22ntoffset%5C%22%3A%5C%223%5C%22%2C%5C%22filterTag%5C%22%3A%5C%22%5C%22%2C%5C%22service%5C%22%3A%5C%22%5C%22%2C%5C%22prop%5C%22%3A%5C%22%5C%22%2C%5C%22loc%5C%22%3A%5C%22%5C%22%2C%5C%22start_price%5C%22%3Anull%2C%5C%22end_price%5C%22%3Anull%2C%5C%22startPrice%5C%22%3Anull%2C%5C%22endPrice%5C%22%3Anull%7D%22%7D'
        #         yield scrapy.Request(url=url)

    def parse(self, response: Response):
        selectors = response.css('div.LeftLay--leftContent--AMmPNfB > div.Content--content--sgSCZ12> div > div')

        # # 打印所有的selectors
        # print("Selectors content:", selectors)
        # # 或者逐一打印每一个selector
        # for selector in selectors:
        #     print(selector)

        for selector in selectors:
            item = TaospiderItem()
            # item['title'] = selector.css('div.Title--descWrapper--HqxzYq0 > div > span::text').extract_first()
            texts = selector.css('div.Title--descWrapper--HqxzYq0 > div > span ::text').extract()
            item['title'] = ''.join(texts).strip()

            item['price'] = selector.css(
                'div.Price--priceWrapper--Q0Dn7pN > span.Price--priceInt--ZlsSi_M::text').extract_first()
            item['shop'] = selector.css(
                'div.ShopInfo--shopInfo--ORFs6rK > div.ShopInfo--TextAndPic--yH0AZfx > a::text').extract_first()
            item['location'] = selector.css(
                'div.Price--priceWrapper--Q0Dn7pN > div:nth-child(5) > span::text').extract_first()
            item['deal_count'] = selector.css(
                'div.Card--mainPicAndDesc--wvcDXaK > div.Price--priceWrapper--Q0Dn7pN > span.Price--realSales--FhTZc7U::text').extract_first()
            yield item
