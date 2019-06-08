import scrapy
from tutorial.items import TutorialItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/",
    ]

    def parse(self, res):
        for href in res.css(".results.categories>.section-wrapper>.children>.cat-list>.cat-item>a::attr('href')"):
            print(res.urljoin(href.extract()))
            url = res.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)


    def parse_dir_contents(self, res):
        for sel in res.xpath("//*[contains(@class, 'title-and-desc')]"):
            item = TutorialItem()
            item["title"] = sel.xpath("a/*[contains(@class, 'site-title')]/text()").extract()
            item["link"] = sel.xpath('a/@href').extract()
            item["desc"] = sel.xpath("normalize-space(*[contains(@class, 'site-descr')]/text())").extract()
            yield item

