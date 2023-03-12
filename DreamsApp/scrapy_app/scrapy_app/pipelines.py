# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2
from dotenv import load_dotenv
import os

class DreamAppPipeline:
    def __init__(self) -> None:
        load_dotenv()
        hostname = os.environ['hostname'] #fill in using os env
        username= os.environ['username'] #fill in using os env
        password= os.environ['password'] # fill in using os env
        database = os.environ['database'] #fill in using os env

        self.connection = psycopg2.connect(host=hostname, user= username, password=password,dbname= database)

        self.cur = self.connection.cursor()

        self.cur.execute("""
        CREATE TABLE if not exists main_dream(
            id text PRIMARY KEY,
            date text,
            quote text
        );
        """)

        pass
    def process_item(self, item, spider):
        self.cur.execute("select * from main_dream where id = %s;",(item['id'],))
        result = self.cur.fetchone()
        if result:
            spider.logger.warn("Item already in database: %s" % item['id'])
        else:
            self.cur.execute("""INSERT INTO main_dream(id,date,quote) VALUES(%s,%s,%s);""",(
                item["id"],
                item["date"],
                item["quote"]
            ))
            self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()