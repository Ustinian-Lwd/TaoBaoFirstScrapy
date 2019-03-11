# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from TaoBaoFirstScrapy.items import TaobaofirstscrapyItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']


    # https://s.taobao.com/search?q=小米&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=&ie=utf8&initiative_id=tbindexz_20170306
    # https://s.taobao.com/search?q=小米&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
    # https://s.taobao.com/search?q=%E5%B0%8F%E7%B1%B3&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48&s=88
    base_url = 'https://s.taobao.com/search?q='
    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + urllib.parse.quote(keyword)
                yield scrapy.Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)


    def parse(self, response):
        products = response.xpath(
            '//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]')
        for product in products:
            item = TaobaofirstscrapyItem()
            item['price'] = ''.join(product.xpath('.//div[contains(@class, "price")]//text()').extract()).strip()
            item['title'] = ''.join(product.xpath('.//div[contains(@class, "title")]//text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div[contains(@class, "shop")]//text()').extract()).strip()
            item['image'] = ''.join(product.xpath('.//div[@class="pic"]//img[contains(@class, "img")]/@data-src').extract()).strip()
            item['deal'] = product.xpath('.//div[contains(@class, "deal-cnt")]//text()').extract_first()
            item['location'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()
            yield item
