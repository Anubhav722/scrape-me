# -*- coding: utf-8 -*-
import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_population']

    def parse(self, response):
    	table = response.xpath('//table')[1]
        pass
