# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaofirstscrapyItem(scrapy.Item):
    # Mongodb、或者是mysql数据表的名称
    collection = table =  'products'

    # 商品图片链接
    image = scrapy.Field()
    # 商品价格
    price = scrapy.Field()
    # 商品购买人数
    deal = scrapy.Field()
    # 商品名称
    title = scrapy.Field()
    # 店铺名称
    shop = scrapy.Field()
    # 店铺所在地
    location = scrapy.Field()

