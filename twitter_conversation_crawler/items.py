# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitterConversationSpyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    username = scrapy.Field()
    content = scrapy.Field()
    replyto = scrapy.Field()
    permalink = scrapy.Field()

    pass
