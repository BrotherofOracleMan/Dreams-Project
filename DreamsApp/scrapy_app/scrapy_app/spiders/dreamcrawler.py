import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

"""
class DreamcrawlerSpider(scrapy.Spider):
    name = "dreamcrawler"
    allowed_domains = ["www.dreambank.net"]

    def start_requests(self):
        urls = ["https://www.dreambank.net/random_sample.cgi?series=b&min=50&max=300&n=5000"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        self.logger("A response has arrived")
        yield response.css('body span::text').getall()
"""
class DreamcrawlerSpider(scrapy.Spider):
    name = "dreamcrawler"

    def start_requests(self):
        urls = ["https://www.dreambank.net/random_sample.cgi?series=b&min=50&max=300&n=5000"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #ToDo:rename this function
    #helper function
    def pairwise(self,it):
        it = iter(it)
        while True:
            try:
                yield next(it) , next(it)
            except StopIteration:
                return
    #ToDo: create a helper function that returns string, id, date
    def parse(self, response):
        data = []
        raw_data = response.css('body span::text').getall()
        for a,b in self.pairwise(raw_data):
            #Split a into ID and date
            id, date = a.split(" ")
            string, id, date = re.sub("\(.*?\)|\[.*?\]","", b).strip() , id.replace("#","").strip() , re.sub(r'[()]','',date.strip())
            data.append((id,date,string))
        self.logger.info(data)
        yield
        {
            'data': data,
        }
