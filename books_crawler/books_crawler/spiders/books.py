# -*- coding: utf-8 -*-

# from scrapy.spiders import CrawlSpider, Rule
from scrapy import Spider
from scrapy.linkextractors import LinkExtractor
# from scrapy.selector import Selector
from scrapy.http import Request

# Selenium imports
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from time import sleep

class BooksSpider(Spider):
	name = 'books'
	allowed_domains = ['books.toscrape.com']
	start_urls = ['http://books.toscrape.com']

	def parse(self, response):
		book_urls = response.xpath('//h3/a/@href').extract()

		for book_url in book_urls:
			absolute_url = response.urljoin(book_url)
			yield Request(absolute_url, callback=self.parse_book)

		# Process next page
		next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
		absolute_next_page_url = response.urljoin(next_page_url)
		yield Request(absolute_next_page_url)


	def parse_book(self, response):
		book_title = response.xpath('//h1/text()').extract_first()
		book_price = response.xpath('//*[@class="price_color"]/text()').extract_first()
		book_image_url = response.xpath('//img/@src').extract_first()

		# u'../../media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg'

		# full image url here
		# http://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg

		book_image_url = book_image_url.replace('../../', 'http://books.toscrape.com/')

		book_rating = response.xpath('//*[contains(@class, "star-rating")]/@class').extract_first()
		book_rating = book_rating.replace('star-rating ', '')

		book_description = response.xpath('//*[@id="product_description"]/following-sibling::p/text()').extract_first()

		yield {
			"book_title": book_title,
			"book_price": book_price,
			"book_image_url": book_image_url,
			"book_rating": book_rating,
			"book_description": book_description
		}



# =========================================
# CODE USING SELENIUM
# =========================================

# class BooksSpider(Spider):
#     name = 'books'
#     allowed_domains = ['books.toscrape.com']

#     def start_requests(self):
#     	# import ipdb; ipdb.set_trace()
#     	# we won't get the response since start_urls is not defined.
#     	self.driver = webdriver.Chrome('/home/sheron/Downloads/chromedriver')
#     	self.driver.get('http://books.toscrape.com')

#     	# Creating a selector
#     	sel = Selector(text=self.driver.page_source)
#     	book_urls = sel.xpath('//h3/a/@href').extract()

#     	for book_url in book_urls:
#     		url = 'http://books.toscrape.com/' + book_url
#     		yield Request(url, callback=self.parse_book)


#     	while True:
#     		try:
#     			next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
#     			sleep(3)
#     			self.logger.info('Sleeping for 3 seconds')
#     			next_page.click()

#     			sel = Selector(text=self.driver.page_source)
#     			book_urls = sel.xpath('//h3/a/@href').extract()

#     			for book_url in book_urls:
#     				url = 'http://books.toscrape.com/catalogue/' + book_url


#     				yield Request(url, callback=self.parse_book)

#     		except NoSuchElementException:
#     			self.logger.info('No more pages to load.')
#     			self.driver.quit()
#     			break

#     def parse_book(self, response):
#     	pass



# =======================================
# Using CrawlSpider here.
# =======================================

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
