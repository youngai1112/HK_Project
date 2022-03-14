import scrapy


class ExampleSpider(scrapy.Spider):     # class 명은 자유기재, scrapy.Spider을 상속받아야 한다. 
    name = 'spider'                     # Spider를 지정할 수 있는 unique한 name을 지정
    allowed_domains = ['https://www.naver.com/']    # 사용될 메인 도메인
    # 실제 스크랩을 진행할 url을 start_urls에 지정
    start_urls = ['https://finance.naver.com/news/news_search.naver?rcdate=&q=%B9%DD%B5%B5%C3%BC&x=27&y=6&sm=title.basic&pd=1&stDateStart=1997-01-01&stDateEnd=2022-03-14']

    # 실제로 spider가 동작을 하게되는 구문
    #   start_urls에 가서 하게 될 동작을 지정
    def parse(self, response):
        filename = response.url.split("=")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)