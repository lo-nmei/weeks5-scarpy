# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from items import PageItem


class FlaskSpider(CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/0.12/']

    links=LinkExtractor(allow=('http://flask.pocoo.org/docs/0.12/.*'))
    rules = [
            Rule(links, callback='parse_page', follow=True),
            ]


    def parse_page(self, response):
        item = PageItem()
        item['url'] = response.url
        item['text'] = response.xpath('//text()').extract()
        yield item

