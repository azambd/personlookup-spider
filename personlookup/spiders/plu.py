# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import PersonlookupItem



class PluSpider(CrawlSpider):
    name = 'plu'
    allowed_domains = ['personlookup.com.au']
    #start_urls = ['https://personlookup.com.au/search?country_id=1&q=1&search=true&state_id=']

    def start_requests(self):
        #For testing it in localhost I used only 20 pages
        for i in range(1, 21):
            url = "https://personlookup.com.au/search?country_id=1&q=1&search=true&state_id=&page={0}".format(i)
            print url
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):

        item = PersonlookupItem()
        rows = response.xpath('//tr')
        for row in rows:
            item['name'] = row.xpath('td/a/text()').extract()
            address = row.xpath('td[2]/text()').extract()
            try:
                if address:
                    item['address'] = address
                    temp_address = ' '.join(address).split(',')
                    item['street'] = temp_address[0]
                    item['suburb'] = temp_address[1].strip()
                    temp_st_zip = temp_address[2].strip()
                    temp_st_zip = temp_st_zip.split(' ')
                    item['state'] = temp_st_zip[0]
                    item['zip_code'] = temp_st_zip[1]
            except:
                pass
            item['telephone'] = row.xpath('td[3]/text()').extract()
            temp_link = row.xpath('td/a/@href').extract()
            item['link'] = response.urljoin(''.join(temp_link))

            yield item
