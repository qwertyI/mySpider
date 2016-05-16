import scrapy
from dotamax_spider.items import TesterhomeSpiderItem
from scrapy.contrib.loader import ItemLoader
import re


class TesterhomeSpider(scrapy.spiders.Spider):
    name = "testerhome"
    allowed_domains = ["testerhome.org"]
    start_urls = [
        'http://testerhome.com'
    ]

    def parse(self, response):
        for sel in response.xpath('//div[contains(@class,"topic media topic")]'):
            item = TesterhomeSpiderItem()
            item['topic_title'] = sel.xpath('div/div[contains(@class,"title media-heading")]/a/text()').extract()
            item['topic_author'] = sel.xpath('div/div[contains(@class,"info")]/a/@data-name').extract()
            item['topic_class'] = sel.xpath('div/div[contains(@class,"info")]/a[contains(@class,"node")]/text()').extract()
            item['topic_reply_num'] = sel.xpath('div[contains(@class,"count media-right")]/a/text()').extract()
            item['topic_author_img'] = sel.xpath('div/a/img/@src').extract()
            yield item
        # l = ItemLoader(item=item, response=response)
        # l.add_xpath('topic_title', '//div/div/div[contains(@class,"title media-heading")]/a/text()')
        # l.add_xpath('topic_author', '//div/div/div[contains(@class,"info")]/a/@data-name')
        # l.add_xpath('topic_class', '//div/div/div[contains(@class,"info")]/a[contains(@class,"node")]/text()')
        # l.add_xpath('topic_reply_num', '//div/div[contains(@class,"count media-right")]/a/text()')
        # return l.load_item()
