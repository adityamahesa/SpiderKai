# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from json import dumps


class BookingPipeline(object):
    collection = []

    def process_item(self, item, spider):
        if spider.name is 'bookingspider':
            self.collection.append(item)
        return item

    def close_spider(self, spider):
        from os import path, makedirs
        dirname = 'json'
        if not path.isdir(dirname):
            makedirs(dirname)
        with open('./'+dirname+'/booking.json', 'wb') as f:
            f.write(dumps([dict(i) for i in self.collection], indent=4, sort_keys=True)+'\n')
