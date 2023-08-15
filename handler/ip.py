import scrapy

from scrapy import signals
from scrapy.utils.log import configure_logging
# from scrapy.exceptions import CloseSpider

from loguru import logger


configure_logging()
class IPSpider(scrapy.Spider):
    name = "ip_spider"

    def __init__(self, kwargs):
        self.state = "init"
        logger.debug(f"Spider {self.name}: OK")

        logger.debug(f"Spider input: {kwargs}")

    def start_requests(self):
        self.state = "start"
        yield scrapy.Request(
            url="http://checkip.amazonaws.com/",
            method="GET",
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, response):
        self.state = "parse"
        logger.debug(f"My IP: {response.text}")
        yield {"ip": response.text}


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(IPSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        spider.stats = crawler.stats.get_stats()
        return spider

    def spider_closed(self, spider):
        self.state = "OK"
        spider.stats["state"] = self.state
