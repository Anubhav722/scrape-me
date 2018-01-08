# -*- coding: utf-8 -*-

# from scrapy.spiders import CrawlSpider, Rule
from scrapy import Spider
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request

# Selenium imports
from selenium import webdriver


class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
    	# import ipdb; ipdb.set_trace()
    	# we won't get the response since start_urls is not defined.
    	self.driver = webdriver.Chrome('/home/sheron/Downloads/chromedriver')
    	self.driver.get('http://books.toscrape.com')

    	# Creating a selector
    	sel = Selector(text=self.driver.page_source)
    	book_urls = sel.xpath('//h3/a/@href').extract()

    	for book_url in book_urls:
    		url = 'http://books.toscrape.com/' + book_url
    		yield Request(url, callback=self.parse_book)

    def parse_book(self, response):
    	pass


# Using CrawlSpider here.
# class BooksSpider(CrawlSpider):
#     name = 'books'
#     allowed_domains = ['books.toscrape.com']
#     start_urls = ['http://books.toscrape.com/']

#     # passing args
#     # rules = (Rule(LinkExtractor(deny_domains=('google.com')), callback='parse_page', follow=True),)
#     rules = (Rule(LinkExtractor(allow=('music')), callback='parse_page', follow=True),)

#     # rules = (Rule(LinkExtractor(), callback='parse_page', follow=True),)

#     def parse_page(self, response):
#         pass
