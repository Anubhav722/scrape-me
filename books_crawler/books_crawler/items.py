# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_title = scrapy.Field()
    book_price = scrapy.Field()

    # Two vars which media pipelines offer.
    # The variable names are very important
    # If you change it, it wont work
    image_urls = scrapy.Field()
    images = scrapy.Field()
