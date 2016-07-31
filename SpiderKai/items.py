# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    tanggal = scrapy.Field()
    origination = scrapy.Field()
    destination = scrapy.Field()
    adult = scrapy.Field()
    infant = scrapy.Field()
    train_no = scrapy.Field()
    train_name = scrapy.Field()
    train_dep_date = scrapy.Field()
    train_dep_time = scrapy.Field()
    train_arv_date = scrapy.Field()
    train_arv_time = scrapy.Field()
    fare_class = scrapy.Field()
    fare_subclass = scrapy.Field()
    fare_adult = scrapy.Field()
    fare_infant = scrapy.Field()
    ticket_seat = scrapy.Field()
    booking = scrapy.Field()


class OptionsItem(scrapy.Item):
    tanggal = scrapy.Field()
    station = scrapy.Field()
