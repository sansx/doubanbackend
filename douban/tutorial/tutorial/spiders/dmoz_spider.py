import scrapy
from tutorial.items import TutorialItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, res):
        filename = res.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(res.body)
        for sel in res.xpath('//ul/li'):
            item = TutorialItem()
            item["title"] = sel.xpath('a/text()').extract()
            item["link"] = sel.xpath('a/@href').extract()
            item["desc"] = sel.xpath('text()').extract()
            yield item




