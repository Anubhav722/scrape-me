# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from books_crawler.items import BooksCrawlerItem


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
		l = ItemLoader(item=BooksCrawlerItem(), response=response)

		book_title = response.xpath('//h1/text()').extract_first()
		book_price = response.xpath('//*[@class="price_color"]/text()').extract_first()
		book_image_url = response.xpath('//img/@src').extract_first()

		# u'../../media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg'

		# full image url here
		# http://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg

		book_image_url = book_image_url.replace('../../', 'http://books.toscrape.com/')

		l.add_value('book_title', book_title)
		l.add_value('book_price', book_price)
		l.add_value('image_urls', book_image_url)

		return l.load_item()