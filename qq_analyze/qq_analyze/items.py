# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqAnalyzeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


#存放说说的类
class Talk(scrapy.Item):
    content=scrapy.Field()#内容
    time=scrapy.Field()#发布时间

