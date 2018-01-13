# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class SubjectsSpider(Spider):
    name = 'subjects'
    allowed_domains = ['class-central.com']
    start_urls = ['http://class-central.com/subjects']

    def __init__(self, subject=None):
    	self.subject = subject


    def parse(self, response):
        if self.subject:
        	subject_url = response.xpath('//*[contains(@title, "' + self.subject + '")]/@href').extract_first()
        	subject_url = response.urljoin(subject_url)
        	yield Request(subject_url, callback=self.parse_subject)

        else:
        	self.logger.info('Scraping default subjects')
        	cs_url = response.xpath('//*[contains(@title, "Computer Science")]/@href').extract_first()
        	cs_url = response.urljoin(cs_url)
        	yield Request(cs_url, callback=self.parse_subject)


    def parse_subject(self, response):
    	subject_name = response.xpath('//title/text()').extract_first().split('|')[0].strip()

    	courses = response.xpath('//*[@class="text--charcoal text-2 medium-up-text-1 block course-name"]')

    	for course in courses:
    		course_url = response.urljoin(course.xpath('.//@href').extract_first())
    		course_name = course.xpath('.//text()').extract_first()

    		yield {
    			'subject_name': subject_name,
    			'course_name': course_name,
    			'course_url': course_url
    		}

    	next_page_url = response.urljoin(response.xpath('//*[@rel="next"]/@href').extract_first())
    	yield Request(next_page_url, callback=self.parse_subject)
