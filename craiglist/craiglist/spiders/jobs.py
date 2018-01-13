# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/egr']


    def parse(self, response):
        listings = response.xpath('//li[@class="result-row"]')

        for listing in listings:
            date = listing.xpath('.//*[@class="result-date"]/@datetime').extract_first()
            link = listing.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
            text = listing.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()

            # yield {
            #     'date': date,
            #     'link': link,
            #     'text': text}

            # to transfer the data from parse method to parse_listing use `meta`.
            yield scrapy.Request(link, callback=self.parse_listing,
                                meta={'date':date,
                                      'link': link,
                                      'date': date})

        next_page_url = response.xpath('//*[@class="button next"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

    def parse_listing(self, response):

        # fetching the values from meta passed from above method
        date = response.meta.get('date')
        link = response.meta.get('link')
        text = response.meta.get('text')

        compensation = response.xpath('//*[@class="attrgroup"]/span[1]/b/text()').extract_first()
        employment_type = response.xpath('//*[@class="attrgroup"]/span[2]/b/text()').extract_first()

        job_profile = response.xpath('//*[@id="titletextonly"]/text()').extract_first()

        job_description = response.xpath('//*[@id="postingbody"]/text()').extract()
        job_description = " ".join(job_description)

        yield {'date': date,
               'link': link,
               'text': text,
               'compensation': compensation,
               'employment_type': employment_type,
               'job_profile': job_profile,
               'job_description': job_description}





    # Commented out since it's good to fetch from outer class. and also we want
    # to fetch more details other than just text

    # def parse(self, response):
    #     listings = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()

    #     for listing in listings:
    #       # print(listing)
    #       yield {'Listing': listing}