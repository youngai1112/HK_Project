# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# data를 class 형태로 만들 수 있다. 
#   제일 먼저 items.py를 정의해야 한다. (가지고 올 데이터를 정의)
# 연습 : title, 제목, 설명 -> 수집해야 할 데이터

import scrapy


class TutorialItem(scrapy.Item):    # Item을 만들 때, scrapy.Item을 상속받아야 한다.
    title = scrapy.Field()          # Item을 만들 때, scrapy.Field()를 사용해야 한다. 
    link = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
