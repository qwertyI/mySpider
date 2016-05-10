# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from testerhome_db import Testerhome_Topic, DBSession
import settings
import sys, datetime

reload(sys)
sys.setdefaultencoding('utf-8')

class TesterhomeSpiderPipeline(object):

    def __init__(self):
        self.session = DBSession()

    def process_item(self, item, spider):
        my_topic = Testerhome_Topic(topic_title=item['topic_title'][0].encode('unicode-escape'),
                                    topic_author=item['topic_author'][0].encode('unicode-escape'),
                                    topic_class=item['topic_class'][0].encode('unicode-escape'),
                                    topic_reply_num=item['topic_reply_num'][0].encode('unicode-escape'),
                                    spider_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        try:
            self.session.add(my_topic)
            # print my_topic
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.close()
        # line = json.dumps(dict(deep_item)) + '\n'
        # self.file.write(line)
        # print '==================================='
        # print 'success enter pipeline'
        # print '==================================='
        return item

