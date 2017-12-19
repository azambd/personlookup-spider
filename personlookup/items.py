# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PersonlookupItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    street = scrapy.Field()
    suburb = scrapy.Field()
    state = scrapy.Field()
    zip_code = scrapy.Field()
    telephone = scrapy.Field()
    link = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
