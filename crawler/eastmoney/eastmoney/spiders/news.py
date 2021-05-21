import scrapy

from eastmoney.items import EastmoneyItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['futures.eastmoney.com']
    start_urls = ['http://futures.eastmoney.com/a/ainesc_1.html']
    i = 1

    def parse(self, response):

        name = response.xpath('//*[@id="newsListContent"]/li/a/span[1]/text()').extract()
        url = response.xpath('//*[@id="newsListContent"]/li/a/@href').extract()
        date = response.xpath('//*[@id="newsListContent"]/li/a/span[2]/text()').extract()
        infos = zip(name,url,date)
        for info in infos:
            news = EastmoneyItem()
            news['name'] = info[0]
            news['url'] = info[1]
            news['date'] = info[2]
            yield scrapy.Request(news['url'], callback = self.parse_text, meta = news)
        self.i += 1
        if self.i < 10:
            next_url = self.start_urls[0].replace('1','{}').format(self.i)
            yield scrapy.Request(next_url)

    def parse_text(self, response):
        text = response.xpath('//*[@id="ContentBody"]/p/text()').extract()
        news = response.meta
        news['text'] = ''.join(text)
        #print("parse_text:%s"%news)
        yield news
