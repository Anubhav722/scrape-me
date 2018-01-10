# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotesSpiderPipeline(object):
    def process_item(self, item, spider):
    	return item


    	# Can alter the data over here.
    	# if item['h1_tag']:
    	# 	item['h1_tag'] = item['h1_tag'][0].upper()
     #    return item
