import scrapy
from dotamax_spider.items import TesterhomeSpiderItem, TesterhomeDetailSpiderItem, TesterhomeDetailReplySpiderItem
from dotamax_spider import pipelines
from scrapy.contrib.loader import ItemLoader
import re


class TesterhomeDetailSpider(scrapy.spiders.Spider):
    name = "detail"
    allowed_domains = ["detail.org"]
    start_urls = [
        'http://testerhome.com/topics/50'
    ]
    pipeline=set([
        pipelines.TesterhomeSpiderDetailPipeline
    ])

    def parse(self, response):
        itemdetail = TesterhomeDetailSpiderItem()
        itemdetail['topic_id'] = response.xpath('//a[contains(@class, "likeable")]/@data-id').extract()[0]
        itemdetail['topic_title'] = response.xpath('//div[contains(@class, "media-body")]/h1/text()').extract()[0]
        topic_body = ''
        for i in response.xpath('//div[contains(@class, "panel-body markdown")]/article/p/text()').extract():
            topic_body += i
        # topic_body
        itemdetail['topic_body'] = topic_body
        itemdetail['topic_author'] = response.xpath('//a[contains(@data-author, "true")]/@data-name').extract()[0]
        itemdetail['topic_like_num'] = response.xpath('//a[contains(@class, "likeable")]/@data-count').extract()[0]
        itemdetail['topic_reply_num'] = response.xpath('//div[contains(@class, "total panel-heading")]/b/text()').extract()[0]
        itemdetail['topic_timeago'] = response.xpath('//abbr[contains(@class, "timeago")]/@title').extract()[0]
        yield itemdetail
        # for sel in response.xpath('//div[contains(@class, "infos")]'):
        #     itemreplydetail = TesterhomeDetailReplySpiderItem()
        #     itemreplydetail['topic_reply_author'] = sel.xpath('div[contains(@class, info)]/span[contains(@class, "name")]/a/@data-name').extract()[0]
        #     itemreplydetail['topic_reply_timeago'] = sel.xpath('div[contains(@class, info)]/span[contains(@class, "time")]/abbr/@title').extract()[0]
        #     itemreplydetail['topic_reply_like_num'] = sel.xpath('div[contains(@class, info)]/span[contains(@class, "opts pull-right")]/a[contains(@class, "likeable")]/@data-count').extract()[0]
        #     itemreplydetail['topic_reply_author'] = ''
        #     for i in sel.xpath('div[contains(@class, markdown)]/p/text()').extract():
        #         itemreplydetail['topic_reply_author'] += i
        #     return itemreplydetail

