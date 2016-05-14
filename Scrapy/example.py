import scrapy
from scrapy.crawler import CrawlerProcess


class MyCrawler(scrapy.Spider):
    name = 'naver_crawler'
    start_urls = ['http://www.naver.com']

    def parse(self, response):
        for item in response.css('#media_tab > div > div > div > div > ul > li > a > img::attr(alt)').extract():
            print item


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()