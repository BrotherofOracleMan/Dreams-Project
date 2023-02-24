import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#Todo: transform this to CrawlSpider
class DreamcrawlerSpider(scrapy.Spider):
    name = "dreamcrawler"

    def start_requests(self):
        urls = [
            "https://www.dreambank.net/random_sample.cgi?series=b&min=50&max=300&n=5000"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def quote_generator(self, it):
        it = iter(it)
        while True:
            try:
                yield next(it), next(it)
            except StopIteration:
                return

    def generate_id_date_string(self, date, quote):
        id, date = date.split(" ") 
        return (id.replace("#", "").strip(), \
               re.sub(r'[()]', '', date.strip()), \
               re.sub("\(.*?\)|\[.*?\]", "", quote).strip())
               

    def parse(self, response):
        data = []
        for date, quote in self.quote_generator(response.css('body span::text').getall()):
            data.append(self.generate_id_date_string(date,quote))
        print(data[-1])
        yield
        {
            'data': data,
        }
