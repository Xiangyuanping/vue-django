from re import L
import scrapy
from news.items import NewsItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule



class News163Spider(CrawlSpider):
    name = 'news163'
    allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']
    rules = (
        Rule(LinkExtractor(allow=r"/22/03\d+/*"),
            callback="parse_news",
            follow=True),
    )

    def parse(self, response):
        pass
    
    def parse_news(self, response):
        item = NewsItem()
        item['news_thread'] = response.url.strip().split('/')[-1][:-5]
        self.get_title(response, item)
        self.get_time(response, item)
        self.get_source(response, item)
        self.get_url(response, item)
        self.get_source_url(response, item)
        self.get_title(response, item)
        self.get_text(response, item)
        return item

    def get_title(self, response, item):
        title = response.css('title::text').extract()
        print('*'*20)
        if title:
            print('title:{}'.format(title[0][:-5]))
            item['news_title'] = title[0][:-5]
    
    def get_time(self, response, item):
        time = response.css('.post_time_source').extract()
        if time:
            print('time:{}'.format(time[0][:-5]))
            item['news_time'] = time[0][:-5]

    def get_source(self, response, item):
        source = response.css('#ne_article_source::text').extract()
        if source:
            print('source:{}'.format(source[0]))
            item['news_source'] = source[0]

    def get_source_url(self, response, item):
        source_url = response.css('#ne_article_source::attr(href)').extract()
        if source_url:
            print('source_url:{}'.format(source_url[0]))
            item['source_url'] = source_url[0]

    def get_text(self, response, item):
        text = response.css('#endText').extract()
        if text:
            print('text:{}'.format(text[0]))
            item['news_text'] = text[0]

    def get_url(self, response, item):
        url = response.url
        if url:
            print('text:{}'.format(url))
            item['news_url'] = url