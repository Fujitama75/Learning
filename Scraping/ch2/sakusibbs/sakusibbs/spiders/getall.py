# -*- coding: utf-8 -*-
import scrapy
import pprint
from ..selenium_middleware import *

USER = "JS-TESTER"
PASS = "ipCU12ySxI"


class GetallSpider(scrapy.Spider):
    name = 'getall'
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "sakusibbs.selenium_middleware.SeleniumMiddleware": 0
        }
    }

    def start_requests(self):
        url = 'https://uta.pw/sakusibbs/users.php?action=login'
        selenium_get(url)
        user = get_dom('#user')
        user.send_keys(USER)
        pw = get_dom('#pass')
        pw.send_keys(PASS)

        btn = get_dom('#loginForm input[type=submit]')
        btn.click()

        a = get_dom('.islogin a')
        mypage = a.get_attribute('href')
        print("mypage=", mypage)
        yield scrapy.Request(mypage, self.parse)

    def parse(self, response):
        alist = response.css('ul#mmlist > li a')
        for a in alist:
            url = a.css('::attr(href)').extract_first()
            url2 = response.urljoin(url)
            yield response.follow(
                url2, self.parse_sakuhin
            )

    def parse_sakuhin(self, response):
        title = response.css('title::text').extract_first()
        print("---", title)

        src = response.css('iframe::attr(src)').extract_first()
        src2 = response.urljoin(src)

        req = scrapy.Request(src2, self.parse_download)
        req.meta["title"] = title
        yield req

    def parse_download(self, response):
        title = response.meta["title"]
        fname = title + '.html'
        with open(fname, "wt") as f:
            f.write(response.body)
    
    def closed(self, response):
        selenium_close()
