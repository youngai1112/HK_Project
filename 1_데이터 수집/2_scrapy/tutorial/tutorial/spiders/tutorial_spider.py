import scrapy
from tutorial.items import spiderItem

class ExampleSpider(scrapy.Spider):     # class 명은 자유기재, scrapy.Spider을 상속받아야 한다. 
    name = 'spider'                     # Spider를 지정할 수 있는 unique한 name을 지정
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
            'spider.middlewares.ScrapyWithSeleniumDownloaderMiddleware': 501,
        }
    }

    def start_requests(self):
        url = "https://finance.naver.com/news/news_search.naver?rcdate=&q=%B9%DD%B5%B5%C3%BC&x=10&y=8&sm=title.basic&pd=1&stDateStart=1997-01-01&stDateEnd=2022-03-14&page=1"
        yield scrapy.Request(url, callback=self.parse)

    # 실제로 spider가 동작을 하게되는 구문
    #   start_urls에 가서 하게 될 동작을 지정
    def parse(self, response):
        links = response.xpath("//*[@id='contentarea_left']/div[2]/dl/dt[1]/a/@href").extract()
        links = list(map(response.urljoin, links))
        for link links:
            yield scrapy.Request(link, callback=self.page_parse)

    def page_parse(self, response):
        item = spiderItem()
        for sel in response.xpath('//*[@id="contentarea_left"]/div[2]/dl'):
            title = response.xpath('dt[1]/a/text()').extract()
            item["date"] = response.xpath('dd[1]/span/text()')[2].extract().split()[0]
            item["time"] = response.xpath('dd[1]/span/text()')[2].extract().split()[1]
            item["link"] = response.xpath('dt[1]/a/@href')
            yield item