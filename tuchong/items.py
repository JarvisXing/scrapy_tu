# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TuchongItem(scrapy.Item):
    # define the fields for your item here like:
    userid = scrapy.Field()
    name = scrapy.Field()

    icon_url = scrapy.Field()
    icon = scrapy.Field()
    
    followingcnt = scrapy.Field()
    followerscnt = scrapy.Field()

    location = scrapy.Field()
    desc = scrapy.Field()
    signtime =scrapy.Field()
    blogcnt = scrapy.Field()
    plabels = scrapy.Field()
    ulabels = scrapy.Field()

    equips = scrapy.Field()
    equpic = scrapy.Field()

    timestramp= scrapy.Field()
    