# -*- coding: utf-8 -*-

import os
import glob

# from scrapy.spiders import CrawlSpider, Rule
from scrapy import Spider
from scrapy.linkextractors import LinkExtractor
# from scrapy.selector import Selector
from scrapy.http import Request

# Selenium imports
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from time import sleep

def product_info(response, value):
	return response.xpath('//th[text()="' + value + '"]/following-sibling::td/text()').extract_first()

class BooksSpider(Spider):
	name = 'books'
	allowed_domains = ['books.toscrape.com']
	# start_urls = ['http://books.toscrape.com']

	def __init__(self, category):
		# passing arguments in scrapy to fetch a particular category ok book.
		self.start_urls = [category]

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

		# product information
		book_upc = product_info(response, 'UPC')
		book_product_type = product_info(response, 'Product Type')
		book_price_without_tax = product_info(response, 'Price (excl. tax)')
		book_price_with_tax = product_info(response, 'Price (incl. tax)')
		book_tax = product_info(response, 'Tax')
		book_availability = product_info(response, 'Availability')
		book_no_of_reviews = product_info(response, 'Number of reviews')

		yield {
			"book_title": book_title,
			"book_price": book_price,
			"book_image_url": book_image_url,
			"book_rating": book_rating,
			"book_description": book_description,

			"book_upc": book_upc,
			"book_product_type": book_product_type,
			"book_price_without_tax": book_price_without_tax,
			"book_price_with_tax": book_price_with_tax,
			"book_tax": book_tax,
			"book_availability": book_availability,
			"book_no_of_reviews": book_no_of_reviews
		}

	def close(self, reason):
		csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
		os.rename(csv_file, 'foobar.csv')