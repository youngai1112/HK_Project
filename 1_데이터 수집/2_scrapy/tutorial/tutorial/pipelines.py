# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


# scrapy를 통해서 들고 온 데이터를 후처리 해야할 때 
#   데이터 필터링, 데이터베이스에 입력할 때 

from itemadapter import ItemAdapter


class TutorialPipeline:
    def process_item(self, item, spider):
        return item
