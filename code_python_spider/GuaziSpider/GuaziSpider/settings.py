# Scrapy settings for GuaziSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "GuaziSpider"

SPIDER_MODULES = ["GuaziSpider.spiders"]
NEWSPIDER_MODULE = "GuaziSpider.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "GuaziSpider (+http://www.yourdomain.com)"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3  # 下载延迟
RANDOMIZE_DOWNLOAD_DELAY = True  # 随机化下载延迟
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    'Cookie': 'uuid=95237ad6-70b3-421d-b400-a9a6adeec728; gcinfo=%7B%22g_c%22%3A%2212%22%2C%22g_c_d%22%3A%22bj%22%2C%22g_c_n%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22d_g_c%22%3A%221%22%2C%22l_c%22%3A-1%2C%22l_c_d%22%3A%22www%22%2C%22l_c_n%22%3A%22%22%2C%22s_c%22%3A%2212%22%2C%22s_c_d%22%3A%22bj%22%2C%22s_c_n%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22d_s_c%22%3A%221%22%7D; user_city_id=12; sessionid=36ff524c-de2a-43a6-f3ae-dfeb2e477f00; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; cainfo=%7B%22ca_s%22%3A%22seo_google%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%2295237ad6-70b3-421d-b400-a9a6adeec728%22%7D; puuid=3c424a05-b8b2-4bd1-d788-3da398072283; platform=pc; cityId=10; cityDomain=langfang; cityName=%E5%BB%8A%E5%9D%8A; gzSupportWebp=1; crystal=U2FsdGVkX19pw8HYV8bRvmv1wCIl9p2FNsJicqm5K/4xcwKYm9KePOiWqykuYTsNrmylnZIos2E0+CwP2GFxA/IwLq7zwR7YdzdqwSv1CAnlDlTpSIKpKMB1q2XGoK9no74SnfdSJl+MuD53kg280LbqhxgFnIPgXOglgj/fcABXR63HCxaBvbyaFg9/lsnoP2XmMPFkF/w/9r7Piw+70NqJTqqyyOOV5d3Pb5P0e59q9uaU1KL+6LAahdTD29dO; DATE=1697699443355; ca_s=self; ca_n=self; SECKEY_ABVK=EuySEzfs3QCNSPrJxDAHbS1GfA9SGH13AM5vLl+x+YM%3D; BMAP_SECKEY=alB9BURrsFcQU3rVMnLJTr9kNd38cmjCVR7uk_Vyb5S79F4svUq0cMFidPxKkK_Iy-YZn3hHzOWKW18u59_6DGreMkqAOMhaTG9HLsrLT2OhO-xmBsFLs9i1Zc8DFBraS1vF7Nzi6cSVA57l8ZIiwd59C3COM_-azybJOP76M4FNYK6JpMnAJZEXz1CTaMlu'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "GuaziSpider.middlewares.GuazispiderSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "GuaziSpider.middlewares.GuazispiderDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "GuaziSpider.pipelines.GuazispiderPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
