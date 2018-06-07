import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy_test.items import TopicItem, ReplierItem


class Myspider(scrapy.Spider):

    name = 'dingdian'
    host = "https://bbs.hupu.com"
    start_urls = [
        "https://bbs.hupu.com/pubg"
    ]

    def parse(self, response):
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        # print(response.text)
        content_list = response.xpath("//*[@class='show-list']/ul/li")
        for content in content_list:
            topicItem = TopicItem()
            topicItem['topic'] = ','.join(content.xpath('div[1]/a').xpath('string(.)').extract())
            topicItem['userid'] = ','.join(content.xpath('div[2]/a').xpath('string(.)').extract())
            topicItem['replier'] = ','.join(content.xpath('div[3]/a').xpath('string(.)').extract())
            print("parse_page==========================================================")
            print(topicItem)
            url = self.host + content.xpath('div[1]/a[1]/@href').extract_first()
            topicItem['url'] = url
            # yield topicItem
            yield Request(url=url, meta={'topic':topicItem['topic']}, callback=self.parse_topic)

    def parse_topic(self, response):
        print("enter parse_topic")
        topic = response.meta.get('topic')
        content_list = response.xpath("//*[@id='readfloor']/div[@class='floor']")
        for content in content_list:
            replier = ReplierItem()
            replier['topic'] = topic
            replier['userid'] = content.xpath("div[@class='floor_box']/div[@class='author']//a/text()").extract_first()
            replier['content'] = content.xpath("div[@class='floor_box']/table[@class='case']").xpath('string(.)').extract_first()
            yield replier