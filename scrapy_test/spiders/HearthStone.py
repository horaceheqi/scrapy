import scrapy
from scrapy.http import Request
from scrapy_test.items import TopicItem, ReplierItem


class HSspider(scrapy.Spider):
    name = 'LianJia_deep'
    host = 'https://sy.lianjia.com'
    start_urls = [
        'https://sy.lianjia.com/ershoufang/pg{}'.format(x) for x in range(1, 2)
    ]

    def parse(self, response):
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        link = response.xpath(".//*[@class='sellListContent']/li")
        for content in link:
            url = content.xpath(".//*[@class='title']/a/@href").extract_first()
            # print(url)
            yield Request(url=url, callback=self.parse_topic)

    def parse_topic(self, response):
        print(response.url)