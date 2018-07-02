# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import json
import redis

class FlasksPipeline(object):
    def process_item(self, item, spider):
        re.sub('html','',item['text'])
        re.sub('(\t\t)+',' ',item['text'])
        self.redis.set('flask:items', json.dumps(item))
        return item


    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
