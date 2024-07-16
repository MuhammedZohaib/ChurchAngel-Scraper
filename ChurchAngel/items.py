import scrapy


class ChurchangelItem(scrapy.Item):
    title = scrapy.Field()
    church_category = scrapy.Field()
    church_tel = scrapy.Field()
    church_description = scrapy.Field()
    church_website = scrapy.Field()
    church_link = scrapy.Field()
    church_category_link = scrapy.Field()
