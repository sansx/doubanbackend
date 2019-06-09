# -*- coding: utf-8 -*-
import scrapy
import re
from tutorial.items import DoubanMovie 

class DoubantopSpider(scrapy.Spider):
    name = 'doubanTop'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    count = 0


    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], headers=self.headers)

    def parse(self, res):
        for href in res.css(".item>.info>.hd>a>span:first-child::text").extract():
            title = "".join(href.split())
            movie = DoubanMovie()
            movie["title"] = title
            yield movie
            pass
        for href in res.css(".thispage").xpath("./following-sibling::*[1]/@href").extract():
            if href :
                # yield scrapy.Request(res.urljoin(href), headers=self.headers)
                pass

        pass
