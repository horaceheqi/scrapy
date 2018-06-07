# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy_test.items import TopicItem, ReplierItem, HomeItem
import os
import time
import csv


class ScrapyTestPipeline(object):
    def __init__(self):
        # csv文件的位置，无需事先创建
        datatime = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
        store_file = os.path.dirname(__file__) + '/csvout/qtw_' + datatime + '.csv'
        # csv写法
        self.file = open(store_file, 'w', encoding='utf-8', newline='')
        self.csvwriter = csv.writer(self.file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        self.csvwriter.writerow(('标题', '地址', '楼层', '关注度', '房本', '总价', '单价'))

    def process_item(self, item, spider):
        if isinstance(item, HomeItem):
            title = item['title']
            name = item['name']
            style = item['style']
            area = item['area']
            orientation = item['orientation']
            decoration = item['decoration']
            floor = item['floor']
            diqu = item['diqu']
            attentionPeople = item['attentionPeople']
            lookNumber = item['lookNumber']
            publicTime = item['publicTime']
            tag = item['tag']
            total_price = item['total_price']
            unit_price = item['unit_price']

            # title = item['title']
            # address = item['address']
            # flood = item['flood']
            # followInfo = item['followInfo']
            # tag = item['tag']
            # totalPrice = item['totalPrice']
            # unitPrice = item['unitPrice']
            self.csvwriter.writerow((title, name, style, area, orientation, decoration, floor, diqu, attentionPeople,
                                     lookNumber, publicTime, tag, total_price, unit_price))

        if isinstance(item, TopicItem):
            item['topic'] = item['topic'].replace("\n", "").replace("\r", "")
            item['replier'] = item['replier'].replace("\n",  "").replace("\r", "")
            item['userid'] = item['userid'].replace("\n", "").replace("\r", "")
            topic = item['topic']
            replier = item['replier']
            userid = item['userid']
            self.csvwriter.writerow((topic, userid, replier))

        if isinstance(item, ReplierItem):
            item['topic'] = item['topic'].replace("\n", "").replace("\r", "")
            item['content'] = item['content'].replace("\n", "").replace("\r", "")
            item['userid'] = item['userid'].replace("\n", "").replace("\r", "")
            topic = item['topic']
            content = item['content']
            userid = item['userid']
            self.csvwriter.writerow((topic, userid, content))
        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
