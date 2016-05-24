import scrapy
from dotamax_spider.items import TesterhomeSpiderItem, TesterhomeDetailSpiderItem, TesterhomeDetailReplySpiderItem
from dotamax_spider import pipelines
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.http import Request
from scrapy.log import logger
from scrapy.contrib.loader import ItemLoader
import re


class TesterhomeDetailSpider(CrawlSpider):
    name = "detail"
    allowed_domains = ["detail.org"]
    start_urls = [
        'http://testerhome.com/topics/1'
    ]
    rules = [
        Rule(sle(allow=("/topics/\d{1,3}")),follow=True,callback='parse')
    ]
    pipeline=set([
        pipelines.TesterhomeSpiderDetailPipeline
    ])

    def parse(self, response):
        with open('./detail.txt', 'wb') as f:
            f.write(response.body)
            f.close()
        itemdetail = TesterhomeDetailSpiderItem()
        itemdetail['topic_id'] = response.xpath('//a[contains(@class, "qrcode")]/@data-url').extract()[0].split('/')[-1]
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
        #     for i in sel.xpath('div[contains(@class, markdown)]/p/text()').extract():
        #         itemreplydetail['topic_reply_author'] += i
        #     yield itemreplydetail

        if int(itemdetail['topic_id']) < 100:
            yield Request('http://testerhome.com/topics/'+str(int(itemdetail['topic_id'])+1), callback=self.parse)
            # self.start_urls.append('http://testerhome.com/topics/'+str(int(itemdetail['topic_id'])+1))
        else:
            logger.info('topic_id > 100')


