import scrapy

import sys

from scrapy.spiders import Spider

from scrapy.selector import HtmlXPathSelector

from companycrawler.items import CompanycrawlerItem

from scrapy.http import Request

from scrapy.selector import Selector
reload(sys)
sys.setdefaultencoding('utf-8')
 

class companycrawler_Spider(scrapy.Spider):
    name = "company_spider"  #spider 이름
    allowed_domains = ["https://www.naver.com/"]  #최상위 도메인
 
    def start_requests(self):
        for i in range(1,201,1):
            yield scrapy.Request("https://finance.naver.com/news/news_search.naver?rcdate=&q=%B9%DD%B5%B5%C3%BC&x=10&y=8&sm=title.basic&pd=1&stDateStart=1997-01-01&stDateEnd=2022-03-14&page={}".format(i),self.parse)
 
    #아이템 parse
    def parse(self, response):
        for column in  response.xpath('//div[@class="filterListArea"]/ul/li') :
            item = CompanycrawlerItem() 
            item['company'] = column.xpath('div/div[@class="coTit"]/a/text()').extract_first()       # 제목 추출
            item['context'] =column.xpath('div/div[@class="tit"]//a/span/text()').extract_first()    # 날짜 추출
            # 시간 추출
            yield item