import scrapy
from collect_data.config.asins import asinList, products_base_url
from scrapy import Request
import scraper_helper as sh


class ProductsSpider(scrapy.Spider):
    name = 'products'
    ransomUserAgent = True

    def startRequests(self):
        for i in asinList:
            yield Request(products_base_url.format(i), meta={'i': i})

    def parse(self, response):
        print(response.request.headers['User-Agent'])
        item = {}
        product_name = response.xpath('normalize-space(//h1[@id="title"]/span/text())').get()
        old_price = response.xpath('normalize-space(//span[@class="priceBlockStrikePriceString a-text-strike"]/text())').get()
        current_price = response.xpath('normalize-space(//span[@id="priceblock_ourprice"]/text())').get()
        deal_price = response.xpath('normalize-space(//span[@id="priceblock_dealprice"]/text())').get()
        categories = response.xpath('//div[@id="wayfinding-breadcrumbs_container"]//span[@class="a-list-item"]/a/text()').getall()
        availability = response.xpath('normalize-space(//div[@id="availability"]/span/text())').get()
        item['product_name'] = product_name
        item['old_price'] = old_price
        item['current_price'] = current_price
        item['deal_price'] = deal_price
        item['category'] = ', '.join(map(lambda x: sh.cleanup(x), categories))
        item['product_availability'] = ''.join(availability).strip()
        yield item
