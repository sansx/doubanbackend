# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from tutorial.config import Config as con
from sqlalchemy import (create_engine, Table, Column, Integer,
String, MetaData, ForeignKey
)


class TutorialPipeline(object):
    def open_spider(self, spider):
        print("mysql+pymysql://root:{}@localhost:3306/test".format(con().passWord))
        engine = create_engine("mysql+pymysql://root:{}@192.168.1.103:3306/test".format(con().passWord), max_overflow=5)
        metadata = MetaData()
        # 定义表
        user = Table('user', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(20)),
            )

        color = Table('color', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(20)),
            )
        # 创建数据表，如果数据表存在，则忽视
        metadata.create_all(engine)

    def process_item(self, item, spider):
        # print(item, spider)
        return item

    def close_spider(self, spider):
        print("close ~~~")
