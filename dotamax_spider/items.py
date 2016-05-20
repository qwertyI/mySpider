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
    topic_author_img = scrapy.Field()
    topic_class = scrapy.Field()
    topic_reply_num = scrapy.Field()

class TesterhomeDetailSpiderItem(scrapy.Item):
    topic_id = scrapy.Field()
    topic_title =scrapy.Field()
    topic_body =scrapy.Field()
    topic_author =scrapy.Field()
    topic_timeago =scrapy.Field()
    topic_like_num =scrapy.Field()
    topic_reply_num =scrapy.Field()

class TesterhomeDetailReplySpiderItem(scrapy.Item):
    topic_reply_author = scrapy.Field()
    topic_reply_timeago = scrapy.Field()
    topic_reply_body = scrapy.Field()
    topic_reply_like_num = scrapy.Field()
