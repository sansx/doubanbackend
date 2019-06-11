# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re
from tutorial.config import Config as con
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, Table, Column, Integer,
                        String, MetaData, ForeignKey, Text, Float
                        )

Base = declarative_base()


class doubanMV(Base):
    __tablename__ = 'dbMovie'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    rate = Column(Float(4, 2))
    rateNum = Column(Integer)


class TutorialPipeline(object):
    def open_spider(self, spider):
        print(
            "mysql+pymysql://root:{password}@localhost:3306/test".format(password=con().password))
        engine = create_engine(
            "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(user=con().user, password=con().password, host=con().host,
                                                                                port=con().port, database=con().database), max_overflow=5)
        metadata = MetaData()
        # 定义表
        Base.metadata.create_all(engine)
        # 创建数据表，如果数据表存在，则忽视
        metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def process_item(self, item, spider):
        print(item['title'], spider)
        ret = self.session.query(doubanMV).filter(
            doubanMV.title == item['title'])
        num = re.match(r"\d+",item['rateNum'])[0]
        if ret.first() is None:
            movie = doubanMV(title=item['title'],
                             rate=item['rate'], rateNum=num)
            self.session.add(movie)
        else:
            movie = ret.update({"rate": item['rate'], "rateNum": num})
        self.session.commit()
        return item

    def close_spider(self, spider):
        self.session.close()
        print("close ~~~")
