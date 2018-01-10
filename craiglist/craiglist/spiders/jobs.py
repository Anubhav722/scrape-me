# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/egr']

    def parse(self, response):
        listings = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

        for listing in listings:
        	# print(listing)
        	yield {'Listing': listing}