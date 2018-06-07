import re
import scrapy
from scrapy.http import Request
from scrapy_test.items import HomeItem


class HomeSpider(scrapy.Spider):
    name = 'LianJia'
    host = 'https://sy.lianjia.com'
    start_urls = [
            'https://sy.lianjia.com/ershoufang/pg{}rs长白岛'.format(x) for x in range(1, 10)
    ]

    def parse(self, response):
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        house_list = response.xpath("//*[@class='sellListContent']/li")
        for house in house_list:
            item = HomeItem()
            item['title'] = ','.join(house.xpath(".//div[@class='title']/a/text()").extract())

            item['name'] = ','.join(house.xpath(".//div[@class='address']/div/a/text()").extract())
            content = ','.join(house.xpath(".//div[@class='address']/div/text()").extract())
            if len(content):
                content = content.split("|")
                item['style'] = content[1]
                item['area'] = content[2]
                item['orientation'] = content[3]
                item['decoration'] = content[4]

            item['floor'] = house.xpath(".//div[@class='flood']/div/text()").re('.{3}')[0]
            item['diqu'] = ','.join(house.xpath(".//div[@class='flood']/div/a/text()").extract())

            content = ','.join(house.xpath(".//div[@class='followInfo']/text()").extract())
            if len(content):
                content = content.split("/")
                if len(content) == 3:
                    item['attentionPeople'] = content[0]
                    item['lookNumber'] = content[1]
                    item['publicTime'] = content[2]

            item['tag'] = ','.join(house.xpath("string(.//div[@class='tag'])").extract())
            item['total_price'] = ','.join(house.xpath("string(.//div[@class='priceInfo']/div[1])").extract())
            item['unit_price'] = ','.join(house.xpath(".//div[@class='priceInfo']/div[2]/span/text()").extract())
            # print(homeMessage)
            yield item