# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from json import dumps


dirname = 'json'


def create_pipeline_dir():
    from os import path, makedirs
    if not path.isdir(dirname):
        makedirs(dirname)


class BookingPipeline(object):
    collection = []

    def process_item(self, item, spider):
        if spider.name is 'bookingspider':
            self.collection.append(item)
        return item

    def close_spider(self, spider):
        if spider.name is 'bookingspider':
            create_pipeline_dir()
            with open('./'+dirname+'/booking.json', 'wb') as f:
                f.write(dumps([dict(i) for i in self.collection], indent=4, sort_keys=True)+'\n')


class OptionsPipeline(object):
    def process_item(self, item, spider):
        if spider.name is 'optionsspider':
            print "This pipeline is activated"
            create_pipeline_dir()
            with open('./'+dirname+'/options.json', 'wb') as f:
                f.write(dumps(dict(item), indent=4, sort_keys=True)+'\n')

