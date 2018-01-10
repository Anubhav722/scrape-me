# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/egr']


    def parse(self, response):
    	listings = response.xpath('//li[@class="result-row"]')

    	for listing in listings:
   			date = listing.xpath('.//*[@class="result-date"]/@datetime').extract_first()
   			link = listing.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
   			text = listing.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()

   			yield {
   				'date': date,
   				'link': link,
   				'text': text
   			}


    # Commented out since it's good to fetch from outer class. and also we want
    # to fetch more details other than just text

    # def parse(self, response):
    #     listings = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

    #     for listing in listings:
    #     	# print(listing)
    #     	yield {'Listing': listing}