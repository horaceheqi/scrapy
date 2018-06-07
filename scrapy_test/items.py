# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TopicItem(scrapy.Item):
    # define the fields for your item here like:
    topic = scrapy.Field()
    userid = scrapy.Field()
    replier = scrapy.Field()
    url = scrapy.Field()


class ReplierItem(scrapy.Item):
    topic = scrapy.Field()
    userid = scrapy.Field()
    content = scrapy.Field()


class HomeItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 小区
    name = scrapy.Field()
    # 结构
    style = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 朝向
    orientation = scrapy.Field()
    # 装修
    decoration = scrapy.Field()
    # 楼梯高度
    floor = scrapy.Field()
    # 地区
    diqu = scrapy.Field()
    # 关注人数
    attentionPeople = scrapy.Field()
    # 查看次数
    lookNumber = scrapy.Field()
    # 发布时间
    publicTime = scrapy.Field()
    tag = scrapy.Field()
    # 总价
    total_price = scrapy.Field()
    # 每平米单价
    unit_price = scrapy.Field()

    # # 电梯
    # elevator = scrapy.Field()
    # # 建造时间
    # build_year = scrapy.Field()
    # # 签约时间
    # sign_time = scrapy.Field()
    # address = scrapy.Field()
    # flood = scrapy.Field()
    # followInfo = scrapy.Field()
    # totalPrice = scrapy.Field()
    # unitPrice = scrapy.Field()