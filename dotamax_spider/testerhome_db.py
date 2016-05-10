from sqlalchemy import Column, String, DateTime,create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import settings

Base = declarative_base()

class Testerhome_Topic(Base):
    __tablename__ = 'testerhome_topic'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    topic_title = Column(String(256))
    topic_author = Column(String(256))
    topic_class = Column(String(256))
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
        return "<Topic(topic_title='%s', topic_author='%s', topic_class='%s', topic_reply_num='%s')>" % (
        self.topic_title, self.topic_author, self.topic_class, self.topic_reply_num)

DBSession = sessionmaker(bind=settings.engine)