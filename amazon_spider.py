import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    p1 = 2
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.flipkart.com/apple-iphone-11-purple-64-gb/product-reviews/itm2b8d03427ddac?pid=MOBFWQ6BTFFJKGKE&lid=LSTMOBFWQ6BTFFJKGKE6U3GXK&marketplace=FLIPKART']

    def parse(self, response):
        items = AmazonItem()  # items store instance of  amazonspiderspider class*****
        s = response.css('._3HqJxg')
        for i in s:
            review_title = i.css('._2-N8zT::text').extract()
            date = i.css('div+ ._2sc7ZR::text').extract()
            review_description = i.css('.t-ZTKy div::text').extract()
            rating = i.css('._1BLPMq::text').extract()
            customer = i.css('._2V5EHH ::text').extract()

            items['review_title'] = review_title
            items['date'] = date
            items['review_description'] = review_description
            items['rating'] = rating
            items['customer'] = customer

            yield items

            next_page='https://www.flipkart.com/apple-iphone-11-purple-64-gb/product-reviews/itm2b8d03427ddac?pid=MOBFWQ6BTFFJKGKE&lid=LSTMOBFWQ6BTFFJKGKE6U3GXK&marketplace=FLIPKART&page=' + str(AmazonSpiderSpider.p1)
            if AmazonSpiderSpider.p1 <= 200:
                AmazonSpiderSpider.p1 +=1
            yield response.follow(next_page, callback=self.parse)
