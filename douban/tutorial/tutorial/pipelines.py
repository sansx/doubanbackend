# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import create_engine, Table, Column, Integer, /
String, MetaData, ForeignKey
import PyMySQL
import tutorial.config as con


class TutorialPipeline(object):
    def process_item(self, item, spider):
        print(item, spider)
        return item

    def open_spider(self, item, spider):
        engine = create_engine("mysql+mysqldb://aaa:{}@localhost:3306/test".format(con.passWord), max_overflow=5)
