#encoding=utf-8
from sqlalchemy import Column, String, DateTime,create_engine, Integer, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotamax_spider import settings
from dotamax_spider.testerhome_db import Testerhome_Topic, DBSession
import sys, datetime

reload(sys)
sys.setdefaultencoding('utf-8')

Base = declarative_base()

class Topic(Base):
    __tablename__ = 'testerhome_topic'

    topic_id = Column(Integer, primary_key=True)
    topic_title = Column(String(40))
    topic_author = Column(String(40))
    topic_class = Column(String(40))
    topic_reply_num = Column(Integer)
    spider_time = Column(DateTime)

    def __init__(self, topic_title, topic_author, topic_class, topic_reply_num, spider_time):
        # self.topic_id = topic_id
        self.topic_title = topic_title
        self.topic_author = topic_author
        self.topic_class = topic_class
        self.topic_reply_num = topic_reply_num
        self.spider_time = spider_time

    def __repr__(self):
        return "<Topic(topic_title='%s', topic_author='%s', topic_class='%s', topic_reply_num='%d')>" % (self.topic_title,self.topic_author,self.topic_class,self.topic_reply_num)

# DBSession = sessionmaker(bind=settings.engine)

session = DBSession()
new_topic = Testerhome_Topic(topic_title='好题目', topic_author='qwerty1', topic_class='spider', topic_reply_num=5, spider_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print new_topic
print session.query(Topic.topic_title).filter_by(topic_id = 20).all()[0][0].decode('unicode-escape')
session.add(new_topic)
session.commit()
session.close()
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# print u'\u597d\u9898\u76ee'.encode('unicode-escape')