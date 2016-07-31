from scrapy import Spider, FormRequest
from SpiderKai import items


class BookingSpider(Spider):
    name = 'bookingspider'
    allowed_domains = ['kereta-api.co.id']
    start_urls = ['https://tiket.kereta-api.co.id/?_it8tnz=Mw==&_8dnts=c2NoZWR1bGU=']

    def parse(self, response):
        yield FormRequest.from_response(response,
                                        formdata={
                                            'tanggal': '20160817#Rabu, 17 Agustus 2016',
                                            'origination': 'KAC#KIARACONDONG',
                                            'destination': 'MN#MADIUN',
                                            'adult': '1',
                                            'infant': '0'
                                        },
                                        callback=self.parseInfo)

    def parseInfo(self, response):
        bookings = response.xpath('//form[contains(@id,\'form_\')]')
        for booking in bookings:
            the_item = items.BookingItem()
            the_item['tanggal'] = booking.xpath('*[@name=\'tanggal\']/@value').extract()[0]
            the_item['origination'] = booking.xpath('*[@name=\'origination\']/@value').extract()[0]
            the_item['destination'] = booking.xpath('*[@name=\'destination\']/@value').extract()[0]
            the_item['adult'] = booking.xpath('*[@name=\'adult\']/@value').extract()[0]
            the_item['infant'] = booking.xpath('*[@name=\'infant\']/@value').extract()[0]
            the_item['train_no'] = booking.xpath('*[@name=\'train_no\']/@value').extract()[0]
            the_item['train_name'] = booking.xpath('*[@name=\'train_name\']/@value').extract()[0]
            the_item['train_dep_date'] = booking.xpath('*[@name=\'train_dep_date\']/@value').extract()[0]
            the_item['train_dep_time'] = booking.xpath('*[@name=\'train_dep_time\']/@value').extract()[0]
            the_item['train_arv_date'] = booking.xpath('*[@name=\'train_arv_date\']/@value').extract()[0]
            the_item['train_arv_time'] = booking.xpath('*[@name=\'train_arv_time\']/@value').extract()[0]
            the_item['fare_class'] = booking.xpath('*[@name=\'fare_class\']/@value').extract()[0]
            the_item['fare_subclass'] = booking.xpath('*[@name=\'fare_subclass\']/@value').extract()[0]
            the_item['fare_adult'] = booking.xpath('*[@name=\'fare_adult\']/@value').extract()[0]
            the_item['fare_infant'] = booking.xpath('*[@name=\'fare_infant\']/@value').extract()[0]
            the_item['ticket_seat'] = booking.xpath('*[@name=\'ticket_seat\']/@value').extract()[0]
            the_item['booking'] = booking.xpath('*[@name=\'booking\']/@value').extract()[0]
            yield the_item


class OptionsSpider(Spider):
    name = 'options'
    allowed_domains = ['kereta-api.co.id']
    start_urls = ['https://tiket.kereta-api.co.id/?_it8tnz=Mw==&_8dnts=c2NoZWR1bGU=']

    def parse(self, response):
        pass

