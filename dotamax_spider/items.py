# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DotamaxSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hero_name = scrapy.Field()

class TesterhomeSpiderItem(scrapy.Item):
    topic_title = scrapy.Field()
    topic_author = scrapy.Field()
    topic_class = scrapy.Field()
    topic_reply_num = scrapy.Field()
