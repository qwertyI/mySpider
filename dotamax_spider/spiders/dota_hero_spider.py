import scrapy
from dotamax_spider.items import DotamaxSpiderItem
import re


class DotaHeroSpider(scrapy.spiders.Spider):
    name = "dotahero"
    allowed_domains = ["dotahero.org"]
    start_urls = [
        'http://dotamax.com/hero/'
    ]

    def parse(self, response):
        pattern = re.compile("DoNav('(.*?)')", re.S)
        for sel in response.xpath('//div[contains(@class,"hero-list-bar")]/span/text()'):
            item = DotamaxSpiderItem()
            item['hero_name'] = sel.extract()
            yield item
