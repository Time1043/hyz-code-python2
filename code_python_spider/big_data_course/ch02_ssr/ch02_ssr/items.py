import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    rank = scrapy.Field()
    label = scrapy.Field()
    area = scrapy.Field()
    time = scrapy.Field()
    duration = scrapy.Field()
