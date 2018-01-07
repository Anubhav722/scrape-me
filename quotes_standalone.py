# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest
# Not required for debugging

class QuotesSpider(Spider):
    name = 'quotes'

    # Commented out to account for logging in.
    # allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['http://quotes.toscrape.com/']

    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
    	token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
    	return FormRequest.from_response(response,
    									 formdata={'csrf_token': token,
    									 			'username': 'foo',
    									 			'password': 'bar'},
    									 callback=self.scrape_home_page)

    def scrape_home_page(self, response):
    	h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        print(h1_tag)
        print(tags)
