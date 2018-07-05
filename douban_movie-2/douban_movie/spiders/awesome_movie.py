# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import Linkextractor
from douban_movie.items import DoubanMovieItem
import re


class AwesomeMovieSpider(CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/subject/3011091/']

    links = LinkExtractor(allow='http://movie.douban.com/subject/\d+/?from=subject-page')
    ruls = [
            Rule(start_urls, callback="parse_start_url"),
            Rule(links, callback="parse_page", follow=True),
            ]
    def parse_movie_item(self, response):
        item = DoubanMovieItem()
        score = response.css('div.rating_self strong ::text').extract_first()
        if score > 8:
            item['url'] = response.url
            item['name'] = response.css('h1 span ::text').extract_first()
            item['summary'] = response.css('span.v:summary ::text').extract_first().strip()
            item['score'] = score
            
        else:
            pass
        yield item

    def parse_start_url(self,response):
        yield self.parse_movie_item(response)

    def parse_page(self, response):
        yield self.parse_movie_item(response)
