# -*- coding: utf-8 -*-
import scrapy
import validators

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider


class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['amazon.com']
    start_urls = ['https://amazon.com/']
    base_url = 'https://amazon.com'
    base_domain = 'amazon.com'
    words = ['virtue', 'signalling', 'is', 'society\'s', 'version', 'proof', 'of', 'stake']
    found_words = set()
    visited = {}
    urls = []
    handle_httpstatus_all = True
    page = 0

    def parse(self, response):
        self.page += 1
        self.check()
        self.search(str(response.body))
        self.parse_urls(response)

        print('URLS', len(self.urls), 'PAGE', self.page, 'VISITED', len(self.visited), self.found_words)
        if len(self.urls) > 0:
            next_page_url = self.urls.pop(0)
            self.visited[next_page_url] = True
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_urls(self, response):
        hxs = scrapy.Selector(response)
        all_links = hxs.xpath('*//a/@href').extract()
        for i in all_links:
            if i.startswith('/'):
                i = self.base_url + i
            if self.base_domain not in i:
                continue
            if i not in self.visited:
                if validators.url(i) is True:
                    self.urls.append(i)

    def check(self):
        if len(self.found_words) != len(self.words):
            return False
        print('All words were found')
        raise CloseSpider('Success')

    def search(self, text):
        text = text.lower()
        for word in self.words:
            if not word in self.found_words:
                if word in text:
                    self.found_words.add(word)
                    print('Found a new words:', word)
