import scrapy


class Soseki2Spider(scrapy.Spider):
    name = 'soseki2'
    start_urls = [
        'https://www.aozora.gr.jp/index_pages/person148.html'
    ]

    def parse(self, response):
        li_list = response.css('ol > li a')
        for a in li_list:
            href = a.css('::attr(href)').extract_first()
            text = a.css('::text').extract_first()
            href2 = response.urljoin(href)

            yield {
                'text': text,
                'url': href2
            }
