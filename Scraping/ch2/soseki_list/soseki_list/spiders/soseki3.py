# -*- coding: utf-8 -*-
import scrapy


class Soseki3Spider(scrapy.Spider):
    name = 'soseki3'
    allowed_domains = ['www.aozora.gr.jp']
    start_urls = [
        'https://www.aozora.gr.jp/index_pages/person148.html'
    ]

    def parse(self, response):
        li_list = response.css('ol > li a')
        for a in li_list:
            href = a.css('::attr(href)').extract_first()
            href2 = response.urljoin(href)

            yield response.follow(
                href2, self.parse_card
            )

    def parse_card(self, response):
        title = response.css('title::text').extract_first()
        alist = response.css('table.download tr td a')
        for a in alist:
            href = a.css('::attr(href)').extract_first()
            href2 = response.urljoin(href)

            if href2[-4:] != ".zip":
                continue

            yield {
                'title': title,
                'url': href2
            }
