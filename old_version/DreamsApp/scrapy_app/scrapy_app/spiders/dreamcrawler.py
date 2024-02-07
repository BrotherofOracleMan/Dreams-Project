import scrapy
import re
from scrapy_app.items import DreamItem
from datetime import date

#Todo: transform this to CrawlSpider
class DreamcrawlerSpider(scrapy.Spider):
    name = "dreamcrawler"

    def start_requests(self):
        urls = [
            "https://www.dreambank.net/random_sample.cgi?series=b&min=10&max=50&n=30"]
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
        dream_item = DreamItem()
        cleaned_list=[]
        for data in response.css('body span::text').getall():
            if "[BL]" in data or data.strip().startswith("(") or data.strip().startswith("["):
                continue
            cleaned_list.append(data)

        for date, quote in self.quote_generator(cleaned_list):
            id, date = date.split(" ")
            id = id.replace("#", "").strip()
            quote = re.sub("\(.*?\)|\[.*?\]", "", quote).strip()
            date = re.sub(r'[()]', '', date.strip())
            dream_item['id'] = id
            dream_item['date'] =  date
            dream_item['quote'] = quote
            yield dream_item

