#encoding=utf-8
import requests
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

session = requests.session()
body = session.get('https://testerhome.com/topics/4975')
response = HtmlResponse(url='https://testerhome.com/topics/49')
with open('./topic.txt', 'wb') as f:
    f.write(body.text.encode('utf-8'))

#topic_title
print Selector(text=body.text).xpath('//div[contains(@class, "media-body")]/h1/text()').extract()[0]
print Selector(text=body.text).xpath('//a[contains(@class, "qrcode")]/@data-url').extract()[0].split('/')[-1]
topic_body = ''
for i in Selector(text=body.text).xpath('//div[contains(@class, "panel-body markdown")]/article/p/text()').extract():
    topic_body += i
#topic_body
print topic_body
#topic_author
print Selector(text=body.text).xpath('//a[contains(@data-author, "true")]/@data-name').extract()[0]
#topic_like
print Selector(text=body.text).xpath('//a[contains(@class, "likeable")]/@data-count').extract()[0]
#topic_reply
print Selector(text=body.text).xpath('//div[contains(@class, "total panel-heading")]/b/text()').extract()[0]
#topic_timeago
print Selector(text=body.text).xpath('//abbr[contains(@class, "timeago")]/@title').extract()[0]

for sel in Selector(text=body.text).xpath('//div[contains(@class, "infos")]'):
    print '========================================================='
    #reply_author
    if sel.xpath('div/span[contains(@class, "name")]/text()').extract()[0].strip() == u'匿名':
        print sel.xpath('div/span[contains(@class, "name")]/text()').extract()[0].strip()
    else:
        print sel.xpath('div/span[contains(@class, "name")]/a/@data-name').extract()[0].strip()
    #reply_time
    print sel.xpath('div/span[contains(@class, "time")]/abbr/@title').extract()[0]
    #reply_like
    print sel.xpath('div/span[contains(@class, "opts pull-right")]/a[contains(@class, "likeable")]/@data-count').extract()[0]
    #reply_body
    reply_body = ''
    for i in sel.xpath('div[contains(@class, markdown)]/p/text()').extract():
        reply_body += i
    print reply_body